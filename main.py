import typer
from rich import print

from agent.core import Agent

app = typer.Typer()


@app.command()
def run(
    task: str,
    debug: bool = typer.Option(False, "--debug", help="Show agent debug trace")
):
    agent = Agent(debug=debug)

    print("\n[bold green]Running Mini Agent Core...[/bold green]\n")

    result = agent.run(task)

    print(result)


if __name__ == "__main__":
    app()