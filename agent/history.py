import json
from pathlib import Path


class History:

    def __init__(self, history_file: str = "history.json", max_messages: int = 10):
        self.history_path = Path(history_file)
        self.max_messages = max_messages

    def load(self) -> list:
        if not self.history_path.exists():
            return []

        try:
            return json.loads(
                self.history_path.read_text(encoding="utf-8")
            )
        except json.JSONDecodeError:
            return []

    def save(self, messages: list):
        messages = messages[-self.max_messages:]

        self.history_path.write_text(
            json.dumps(messages, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def add(self, role: str, content: str):
        messages = self.load()

        messages.append({
            "role": role,
            "content": content
        })

        self.save(messages)

    def clear(self):
        self.save([])
