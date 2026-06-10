import re

from agent.registry import get_tool


class ToolChain:

    def extract_math_expression(self, task: str) -> str:
        match = re.search(
            r"[\d\s\+\-\*\/\(\)\.]+",
            task
        )

        if match:
            return match.group().strip()

        return ""

    def run(
        self,
        tools,
        task,
        agent
    ):

        results = []
        last_result = None
        status = "success"
        error = None

        for tool_name in tools:

            tool_config = get_tool(tool_name)

            if tool_config is None:
                status = "failed"
                error = f"{tool_name}: tool not found"
                results.append(error)
                break

            tool_func = tool_config["function"]

            if tool_name == "calculator":

                expression = self.extract_math_expression(task)

                if not expression:
                    status = "failed"
                    error = "calculator failed: no valid math expression found"
                    results.append(error)
                    break

                result = tool_func(expression)

                if result.startswith("Error"):
                    status = "failed"
                    error = f"calculator failed: {result}"
                    results.append(error)
                    break

                last_result = result
                results.append(
                    f"calculator -> {expression} = {result}"
                )

            elif tool_name == "note_writer":

                if last_result:
                    content = f"""
Task:
{task}

Result:
{last_result}
"""
                else:
                    content = agent.ask_llm(task)

                result = tool_func(
                    "agent_note.md",
                    content
                )

                results.append(result)

        return {
            "status": status,
            "error": error,
            "results": results,
            "last_result": last_result
        }