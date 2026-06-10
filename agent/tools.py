from pathlib import Path


def calculator(expression: str):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def note_writer(filename: str, content: str):
    notes_dir = Path("notes")
    notes_dir.mkdir(exist_ok=True)

    file_path = notes_dir / filename
    file_path.write_text(content, encoding="utf-8")

    return f"Note saved to {file_path}"