class DebugTrace:

    def __init__(self, enabled=False):
        self.enabled = enabled
        self.events = []

    def add(self, event: str, data=None):
        if not self.enabled:
            return

        self.events.append({
            "event": event,
            "data": data
        })

    def render(self) -> str:
        if not self.enabled:
            return ""

        output = ["\nDebug Trace:\n"]

        for index, item in enumerate(self.events, start=1):
            output.append(f"{index}. {item['event']}")

            if item["data"] is not None:
                output.append(f"   {item['data']}")

        return "\n".join(output)
