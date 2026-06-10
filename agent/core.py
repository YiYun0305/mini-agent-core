from ollama import chat

from agent.memory import Memory
from agent.router import Router
import agent.tools
from agent.registry import get_tool


class Agent:

    def __init__(self, model="qwen3:8b"):
        self.model = model
        self.memory = Memory()
        self.router = Router()

    def should_remember(self, task: str) -> bool:
        keywords = ["记住"]
        return any(keyword in task for keyword in keywords)

    def should_recall(self, task: str) -> bool:
        keywords = [
            "我的项目叫什么",
            "我叫什么",
            "我住哪里",
            "我记住了什么"
        ]

        return any(keyword in task for keyword in keywords)

    def parse_memory_save(self, task: str):

        mappings = {
            "记住项目名：": "project",
            "记住姓名：": "name",
            "记住城市：": "city",
        }

        for prefix, key in mappings.items():

            if task.startswith(prefix):

                value = task.replace(
                    prefix,
                    ""
                ).strip()

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

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": f"""
You are Mini Agent Core.

Answer clearly and briefly.

Do not show internal reasoning.

User memory:
{memory_data}
"""
                },
                {
                    "role": "user",
                    "content": task
                }
            ],
            options={
                "temperature": 0.3
            }
        )

        return response["message"]["content"]

    def execute_tool(self, tool_name: str, task: str) -> str:

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

        # Structured Memory Save
        if self.should_remember(task):

            parsed = self.parse_memory_save(task)

            if parsed:

                key, value = parsed

                result = self.memory.save(
                    key,
                    value
                )

                return f"""
Agent Thinking:
Structured memory detected

Result:
{result}
"""

            return """
Agent Thinking:
Memory format not supported
"""

        # Structured Memory Recall
        if self.should_recall(task):

            result = self.handle_memory_recall(
                task
            )

            return f"""
Agent Thinking:
Memory recall requested

Result:
{result}
"""

        # Tool Routing
        tool_name = self.router.route(task)

        if tool_name:
            return self.execute_tool(
                tool_name,
                task
            )

        # Default LLM with Memory Context
        return self.ask_llm(task)