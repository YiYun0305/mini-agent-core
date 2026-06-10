from agent.tool_selector import ToolSelector
from agent.toolchain import ToolChain


class Executor:

    def __init__(self, agent):
        self.agent = agent
        self.tool_selector = ToolSelector()
        self.tool_chain = ToolChain()

    def execute(self, task: str, plan: str) -> dict:

        selected_tools = self.tool_selector.select(task)

        self.agent.debug_trace.add(
            "Tools selected",
            selected_tools
        )

        if not selected_tools:
            return {
                "status": "skipped",
                "tools": [],
                "result": "No executable tools selected.",
                "plan": plan
            }

        chain_result = self.tool_chain.run(
            selected_tools,
            task,
            self.agent
        )

        self.agent.debug_trace.add(
            "Tool chain result",
            chain_result
        )

        return {
            "status": chain_result["status"],
            "tools": selected_tools,
            "result": chain_result["results"],
            "error": chain_result["error"],
            "last_result": chain_result["last_result"],
            "saved_file": chain_result.get("saved_file"),
            "plan": plan
        }