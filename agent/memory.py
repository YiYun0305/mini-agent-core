from pathlib import Path


class Memory:
    def __init__(self, memory_file: str = "memory.txt"):
        self.memory_path = Path(memory_file)

    def save(self, content: str):
        with self.memory_path.open("a", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        return "Memory saved."

    def load(self) -> str:
        if not self.memory_path.exists():
            return ""

        return self.memory_path.read_text(encoding="utf-8")
