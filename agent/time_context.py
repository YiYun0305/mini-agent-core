from datetime import datetime


class TimeContext:

    def __init__(self):
        self.now = datetime.now()

    def current_date(self) -> str:
        return self.now.strftime("%Y-%m-%d")

    def current_year(self) -> int:
        return self.now.year

    def current_month(self) -> int:
        return self.now.month

    def current_day(self) -> int:
        return self.now.day

    def as_prompt_context(self) -> str:
        return f"""
Current date: {self.current_date()}
Current year: {self.current_year()}
Current month: {self.current_month()}
Current day: {self.current_day()}
"""
