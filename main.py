import typer
from rich import print

from agent.core import Agent

app = typer.Typer()


@app.command()
def run(task: str):
    agent = Agent()

    print("\n[bold green]Running Mini Agent Core...[/bold green]\n")

    result = agent.run(task)

    print(result)


if __name__ == "__main__":
    app()
