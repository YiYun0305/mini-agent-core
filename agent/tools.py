from pathlib import Path

from ddgs import DDGS

from agent.registry import tool
from agent.search_rewriter import SearchQueryRewriter


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

    file_path = notes_dir / filename
    file_path.write_text(content, encoding="utf-8")

    return f"Note saved to {file_path}"


@tool(
    name="web_search",
    description="Search the web for recent or real-time information."
)
def web_search(query: str):
    try:
        rewriter = SearchQueryRewriter()
        rewritten_query = rewriter.rewrite(query)

        results = []

        with DDGS() as ddgs:
            for r in ddgs.text(
                rewritten_query,
                max_results=8
            ):
                results.append(
                    f"Title: {r.get('title', '')}\n"
                    f"Body: {r.get('body', '')}\n"
                    f"URL: {r.get('href', '')}\n"
                )

        if not results:
            return f"No search results found for: {rewritten_query}"

        return (
            f"Original Query: {query}\n"
            f"Rewritten Query: {rewritten_query}\n\n"
            + "\n".join(results)
        )

    except Exception as e:
        return f"Error: {e}"