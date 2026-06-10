from ollama import chat


class QueryRewriter:

    def __init__(self, model="qwen3:8b"):
        self.model = model

    def rewrite(self, task: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """
You are a search query rewriting engine.

Convert the user's question into the best web search query.

Rules:
- Return only one search query.
- Do not explain.
- Prefer English search terms.
- Include key entities.
- Include words like latest, today, recent, stock price, weather when needed.
- Do not use Markdown.
"""
                },
                {
                    "role": "user",
                    "content": task
                }
            ],
            options={
                "temperature": 0.1
            }
        )

        return response["message"]["content"].strip()
