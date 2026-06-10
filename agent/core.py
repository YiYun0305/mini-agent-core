from ollama import chat

from agent.memory import Memory
from agent.history import History
from agent.router import Router
from agent.planner import Planner
from agent.executor import Executor
from agent.loop import AgentLoop
from agent.debug import DebugTrace

import agent.tools
from agent.registry import get_tool


class Agent:

    def __init__(self, model="qwen3:8b", debug=False):
        self.model = model
        self.memory = Memory()
        self.history = History()
        self.router = Router()
        self.planner = Planner(model)
        self.debug_trace = DebugTrace(enabled=debug)
        self.executor = Executor(self)
        self.loop = AgentLoop(self)

    def should_remember(self, task: str) -> bool:
        return "记住" in task

    def should_recall(self, task: str) -> bool:
        keywords = [
            "我的项目叫什么",
            "我叫什么",
            "我住哪里",
            "我记住了什么"
        ]
        return any(keyword in task for keyword in keywords)

    def should_plan(self, task: str) -> bool:
        keywords = ["计划", "规划", "方案", "plan"]
        return any(keyword in task.lower() for keyword in keywords)

    def should_execute_plan(self, task: str) -> bool:
        keywords = [
            "保存",
            "save",
            "今天",
            "最新",
            "新闻",
            "实时",
            "current",
            "latest",
            "today",
            "news"
        ]

        return any(keyword in task.lower() for keyword in keywords)

    def parse_memory_save(self, task: str):
        mappings = {
            "记住项目名：": "project",
            "记住姓名：": "name",
            "记住城市：": "city",
        }

        for prefix, key in mappings.items():
            if task.startswith(prefix):
                value = task.replace(prefix, "").strip()
                return key, value

        return None

    def handle_memory_recall(self, task: str):
        if "我的项目叫什么" in task:
            return self.memory.recall("project")

        if "我叫什么" in task:
            return self.memory.recall("name")

        if "我住哪里" in task:
            return self.memory.recall("city")

        if "我记住了什么" in task:
            return self.memory.load_all()

        return None

    def ask_llm(self, task: str) -> str:
        memory_data = self.memory.load_all()
        history_messages = self.history.load()

        self.debug_trace.add(
            "LLM request",
            {
                "task": task,
                "memory": memory_data,
                "history_count": len(history_messages)
            }
        )

        messages = [
            {
                "role": "system",
                "content": f"""
You are Mini Agent Core.

Answer clearly and briefly.

Do not show internal reasoning.

Do not use Markdown formatting.
Do not use bold markers like **.
Use plain text only.

User memory:
{memory_data}
"""
            }
        ]

        messages.extend(history_messages)

        messages.append(
            {
                "role": "user",
                "content": task
            }
        )

        response = chat(
            model=self.model,
            messages=messages,
            options={"temperature": 0.3}
        )

        content = response["message"]["content"]

        self.history.add("user", task)
        self.history.add("assistant", content)

        self.debug_trace.add(
            "LLM response",
            content[:500]
        )

        return content

    def execute_tool(self, tool_name: str, task: str) -> str:
        self.debug_trace.add(
            "Direct tool execution",
            {
                "tool": tool_name,
                "task": task
            }
        )

        tool_config = get_tool(tool_name)

        if tool_config is None:
            return f"Tool not found: {tool_name}"

        tool_func = tool_config["function"]

        if tool_name == "calculator":
            result = tool_func(task)

            return f"""
Agent Thinking:
Tool selected by router

Tool Selected:
calculator

Result:
{result}
"""

        if tool_name == "note_writer":
            content = self.ask_llm(task)

            result = tool_func(
                "agent_note.md",
                content
            )

            return f"""
Agent Thinking:
Tool selected by router

Tool Selected:
note_writer

{result}

Content:
{content}
"""

        return f"Unsupported tool: {tool_name}"

    def run(self, task: str) -> str:

        self.debug_trace.add(
            "Task received",
            task
        )

        # Conversation History Recall
        if "刚才" in task:
            result = self.ask_llm(task)
            return result + self.debug_trace.render()

        # Structured Memory Save
        if self.should_remember(task):
            parsed = self.parse_memory_save(task)

            if parsed:
                key, value = parsed
                result = self.memory.save(key, value)

                self.debug_trace.add(
                    "Memory saved",
                    {
                        "key": key,
                        "value": value
                    }
                )

                output = f"""
Agent Thinking:
Structured memory detected

Result:
{result}
"""
                return output + self.debug_trace.render()

            output = """
Agent Thinking:
Memory format not supported
"""
            return output + self.debug_trace.render()

        # Structured Memory Recall
        if self.should_recall(task):
            result = self.handle_memory_recall(task)

            self.debug_trace.add(
                "Memory recalled",
                result
            )

            output = f"""
Agent Thinking:
Memory recall requested

Result:
{result}
"""
            return output + self.debug_trace.render()

        # Agent Loop
        if self.should_execute_plan(task):
            self.debug_trace.add(
                "Agent loop selected",
                task
            )
            result = self.loop.run(task)
            return result + self.debug_trace.render()

        # Planner only
        if self.should_plan(task):
            plan = self.planner.create_plan(task)

            self.debug_trace.add(
                "Planner only",
                plan
            )

            output = f"""
Agent Planning:

{plan}
"""
            return output + self.debug_trace.render()

        # Tool Routing
        tool_name = self.router.route(task)

        if tool_name:
            self.debug_trace.add(
                "Router selected tool",
                tool_name
            )

            result = self.execute_tool(tool_name, task)
            return result + self.debug_trace.render()

        # Default LLM
        result = self.ask_llm(task)
        return result + self.debug_trace.render()