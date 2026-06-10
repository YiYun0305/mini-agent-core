class SearchQueryRewriter:

    def rewrite(self, query: str) -> str:

        q = query.lower()

        if "英伟达" in query or "nvidia" in q or "nvda" in q:
            return "NVDA stock price today NVIDIA"

        if "波士顿" in query and "天气" in query:
            return "Boston weather today"

        if "天气" in query:
            return f"{query} weather today"

        if "新闻" in query or "最新" in query or "recent" in q or "latest" in q:
            return f"{query} latest news"

        if "签证" in query or "h1b" in q or "行政审查" in query:
            return f"{query} recent updates forum official"

        return query
