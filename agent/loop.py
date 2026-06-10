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

        saved_files = []

        for item in observations:
            execution = item.get("execution", {})
            saved_file = execution.get("saved_file")

            if saved_file:
                saved_files.append(saved_file)

        final_summary = self.agent.ask_llm(
            f"""
Summarize the final result for the user.

Original task:
{task}

Final status:
{final_status}

Saved files:
{saved_files}

Observations:
{observations}

Rules:
- If files were saved, mention the exact saved file path from Saved files.
- Do not invent file paths.
- Use plain text only.
- Do not use Markdown formatting.
- Do not use bold markers like **.
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