class Router:

    def route(self, task: str):

        math_chars = set("0123456789+-*/(). ")

        if all(char in math_chars for char in task):
            return "calculator"

        if "保存" in task:
            return "note_writer"

        return None
