from agent.tool_selector import ToolSelector
from agent.toolchain import ToolChain


class Executor:

    def __init__(self, agent):
        self.agent = agent
        self.tool_selector = ToolSelector()
        self.tool_chain = ToolChain()

    def execute(self, task: str, plan: str) -> str:

        selected_tools = self.tool_selector.select(
            task
        )

        if not selected_tools:
            return f"""
Executor Result:

No executable tools selected.

Plan:
{plan}
"""

        result = self.tool_chain.run(
            selected_tools,
            task,
            self.agent
        )

        return f"""
Executor Result:

Selected Tools:
{selected_tools}

Tool Chain Result:
{result}

Final Output:
Task completed successfully.
"""