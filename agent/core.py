from ollama import chat

from agent.memory import Memory
from agent.router import Router
from agent.registry import TOOLS


class Agent:

    def __init__(self, model="qwen3:8b"):
        self.model = model
        self.memory = Memory()
        self.router = Router()

    def should_remember(self, task: str) -> bool:
        keywords = ["记住", "remember"]
        return any(keyword in task.lower() for keyword in keywords)

    def should_recall(self, task: str) -> bool:
        keywords = [
            "我记住了什么",
            "我的项目叫什么",
            "memory",
            "remembered"
        ]
        return any(keyword in task.lower() for keyword in keywords)

    def ask_llm(self, task: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """
You are Mini Agent Core.

Answer clearly and briefly.

Do not show internal reasoning.
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
        tool = TOOLS.get(tool_name)

        if tool is None:
            return f"Tool not found: {tool_name}"

        if tool_name == "calculator":
            result = tool(task)

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
            result = tool("agent_note.md", content)

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

        # Memory Save
        if self.should_remember(task):
            self.memory.save(task)

            return """
Agent Thinking:
Memory detected

Result:
Memory saved successfully.
"""

        # Memory Recall
        if self.should_recall(task):
            memory_content = self.memory.load()

            return f"""
Agent Thinking:
Memory recall requested

Memory:
{memory_content}
"""

        # Tool Routing
        tool_name = self.router.route(task)

        if tool_name:
            return self.execute_tool(tool_name, task)

        # Default LLM
        return self.ask_llm(task)