class ToolSelector:

    def select(
        self,
        task
    ):

        tools = []

        # Web Search
        if (
            "今天" in task
            or "最新" in task
            or "新闻" in task
            or "实时" in task
            or "current" in task.lower()
            or "latest" in task.lower()
            or "today" in task.lower()
            or "news" in task.lower()
        ):
            tools.append(
                "web_search"
            )

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