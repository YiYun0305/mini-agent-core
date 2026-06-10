class ToolSelector:

    def select(
        self,
        task
    ):

        tools = []

        if any(
            char.isdigit()
            for char in task
        ):
            tools.append(
                "calculator"
            )

        if (
            "保存" in task
            or "save" in task.lower()
        ):
            tools.append(
                "note_writer"
            )

        return tools
