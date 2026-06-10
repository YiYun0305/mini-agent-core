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

        final_summary = self.agent.ask_llm(
            f"""
Summarize the final result for the user.

Original task:
{task}

Final status:
{final_status}

Observations:
{observations}
"""
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