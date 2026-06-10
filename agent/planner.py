from ollama import chat


class Planner:

    def __init__(self, model="qwen3:8b"):
        self.model = model

    def create_plan(self, task: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """
You are a task planner for an AI Agent.

Break the user's task into clear, concise execution steps.

Do not execute the task.

Return only the plan.
"""
                },
                {
                    "role": "user",
                    "content": task
                }
            ],
            options={
                "temperature": 0.2
            }
        )

        return response["message"]["content"]
