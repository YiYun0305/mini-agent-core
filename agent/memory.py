import json
from pathlib import Path


class Memory:

    def __init__(self, memory_file: str = "memory.json"):
        self.memory_path = Path(memory_file)

    def _load_data(self) -> dict:
        if not self.memory_path.exists():
            return {}

        try:
            return json.loads(
                self.memory_path.read_text(encoding="utf-8")
            )
        except json.JSONDecodeError:
            return {}

    def _save_data(self, data: dict):
        self.memory_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def save(self, key: str, value: str):
        data = self._load_data()
        data[key] = value
        self._save_data(data)

        return f"Memory saved: {key} = {value}"

    def recall(self, key: str):
        data = self._load_data()
        return data.get(key)

    def load_all(self) -> dict:
        return self._load_data()