class AgentLoop:

    def __init__(self, agent, max_steps: int = 3):
        self.agent = agent
        self.max_steps = max_steps

    def run(self, task: str) -> str:

        observations = []

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
                    "result": execution_result
                }
            )

            if "Task completed successfully" in execution_result:
                break

        final_summary = self.agent.ask_llm(
            f"""
Summarize the final result for the user.

Original task:
{task}

Observations:
{observations}
"""
        )

        return f"""
Agent Loop Completed

Steps:
{len(observations)}

Final Summary:
{final_summary}
"""
