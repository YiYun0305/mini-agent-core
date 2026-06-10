from ollama import chat
from agent.tools import calculator, note_writer
from agent.memory import Memory


class Agent:

    def __init__(self, model="qwen3:8b"):
        self.model = model
        self.memory = Memory()

    def is_math_expression(self, task: str) -> bool:
        math_chars = set("0123456789+-*/(). ")
        return all(char in math_chars for char in task)

    def should_save_note(self, task: str) -> bool:
        keywords = ["保存", "写入", "记录", "save", "note"]
        return any(keyword in task.lower() for keyword in keywords)

    def should_remember(self, task: str) -> bool:
        keywords = [
            "记住",
            "remember"
        ]

        return any(
            keyword in task.lower()
            for keyword in keywords
        )

    def should_recall(self, task: str) -> bool:
        keywords = [
            "我记住了什么",
            "我的项目叫什么",
            "memory",
            "remembered"
        ]

        return any(
            keyword in task.lower()
            for keyword in keywords
        )

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

        # Calculator Tool
        if self.is_math_expression(task):

            result = calculator(task)

            return f"""
Agent Thinking:
Detected math expression

Tool Selected:
calculator

Result:
{result}
"""

        # Note Writer Tool
        if self.should_save_note(task):

            content = self.ask_llm(task)

            save_result = note_writer(
                "agent_note.md",
                content
            )

            return f"""
Agent Thinking:
Detected note saving task

Tool Selected:
note_writer

{save_result}

Content:
{content}
"""

        # Default LLM
        return self.ask_llm(task)