from pathlib import Path

from ddgs import DDGS

from agent.registry import tool
from agent.query_rewriter import QueryRewriter
from agent.search_filter import SearchFilter


@tool(
    name="calculator",
    description="Execute simple mathematical expressions."
)
def calculator(expression: str):
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error: {e}"


@tool(
    name="note_writer",
    description="Write generated content to a local markdown note."
)
def note_writer(filename: str, content: str):
    notes_dir = Path("notes")
    notes_dir.mkdir(exist_ok=True)

    base_name = "agent_output"
    extension = ".md"
    index = 1

    while True:
        file_path = notes_dir / f"{base_name}_{index}{extension}"

        if not file_path.exists():
            break

        index += 1

    file_path.write_text(content, encoding="utf-8")

    return f"Note saved to {file_path}"

@tool(
    name="web_search",
    description="Search the web for recent or real-time information."
)
def web_search(query: str):
    try:
        rewriter = QueryRewriter()
        rewritten_query = rewriter.rewrite(query)

        raw_results = []

        with DDGS() as ddgs:
            for r in ddgs.text(
                rewritten_query,
                max_results=10
            ):
                raw_results.append(r)

        search_filter = SearchFilter()
        filtered_results = search_filter.filter_results(
            raw_results,
            max_results=5
        )

        if not filtered_results:
            return (
                f"Original Query: {query}\n"
                f"Rewritten Query: {rewritten_query}\n\n"
                "No high-quality recent search results found."
            )

        formatted_results = []

        for item in filtered_results:
            formatted_results.append(
                f"Title: {item.get('title', '')}\n"
                f"Body: {item.get('body', '')}\n"
                f"URL: {item.get('url', '')}\n"
                f"Source Score: {item.get('score', 0)}\n"
            )

        return (
            f"Original Query: {query}\n"
            f"Rewritten Query: {rewritten_query}\n\n"
            f"Filtered Results:\n"
            + "\n".join(formatted_results)
        )

    except Exception as e:
        return f"Error: {e}"