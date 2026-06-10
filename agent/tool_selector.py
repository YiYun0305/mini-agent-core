class ToolSelector:

    def select(
        self,
        task
    ):

        tools = []

        # Calculator
        if (
            "计算" in task
            or "+" in task
            or "-" in task
            or "*" in task
            or "/" in task
        ):
            tools.append(
                "calculator"
            )

        # Note Writer
        if (
            "保存" in task
            or "save" in task.lower()
        ):
            tools.append(
                "note_writer"
            )

        return tools