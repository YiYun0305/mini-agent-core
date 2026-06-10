from agent.registry import get_tool


class Executor:

    def __init__(self, agent):
        self.agent = agent

    def execute(self, task: str, plan: str) -> str:

        if "保存" in task or "save" in task.lower():

            content = self.agent.ask_llm(
                task.replace("保存", "")
            )

            tool_config = get_tool("note_writer")

            if tool_config is None:
                return "note_writer tool not found."

            note_writer = tool_config["function"]

            save_result = note_writer(
                "agent_note.md",
                content
            )

            return f"""
Executor Result:

Step 1:
Content generated.

Step 2:
{save_result}

Final Output:
Task completed successfully.
"""

        return f"""
Executor Result:

No executable tool flow found.

Plan:
{plan}
"""
