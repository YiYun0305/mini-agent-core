class AgentLoop:

    def __init__(self, agent, max_steps: int = 3):
        self.agent = agent
        self.max_steps = max_steps

    def run(self, task: str) -> str:

        observations = []
        final_status = "failed"

        for step in range(1, self.max_steps + 1):

            plan = self.agent.planner.create_plan(task)

            execution_result = self.agent.executor.execute(
                task,
                plan
            )

            observations.append(
                {
                    "step": step,
                    "plan": plan,
                    "execution": execution_result
                }
            )

            if execution_result["status"] == "success":
                final_status = "success"
                break

            if execution_result["status"] == "failed":
                final_status = "failed"
                break

        execution = observations[-1]["execution"]

        final_summary = execution.get("last_result")

        if not final_summary:

            results = execution.get("result", [])

            if results:
                final_summary = "\n".join(
                    str(item)
                    for item in results
            )
            else:
                final_summary = "No result available."

        saved_file = execution.get(
            "saved_file"
        )

        if saved_file:
            final_summary += (
                f"\n\nResult saved to:\n{saved_file}"
            )

        return f"""
Agent Loop Completed

Status:
{final_status}

Steps:
{len(observations)}

Final Summary:
{final_summary}
"""