from pathlib import Path

from agent.registry import tool


@tool(
    name="calculator",
    description="Execute simple mathematical expressions."
)
def calculator(expression: str):
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error: {e}"


@tool(
    name="note_writer",
    description="Write generated content to a local markdown note."
)
def note_writer(filename: str, content: str):
    notes_dir = Path("notes")
    notes_dir.mkdir(exist_ok=True)

    file_path = notes_dir / filename
    file_path.write_text(content, encoding="utf-8")

    return f"Note saved to {file_path}"