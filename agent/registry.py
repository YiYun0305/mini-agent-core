TOOLS = {}


def tool(name: str, description: str = ""):
    def decorator(func):
        TOOLS[name] = {
            "name": name,
            "description": description,
            "function": func,
        }
        return func

    return decorator


def get_tool(name: str):
    return TOOLS.get(name)


def list_tools():
    return TOOLS