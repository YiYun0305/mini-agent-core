from urllib.parse import urlparse


class SearchFilter:

    HIGH_QUALITY_DOMAINS = {
        "reuters.com": 10,
        "apnews.com": 10,
        "bbc.com": 9,
        "bloomberg.com": 9,
        "cnbc.com": 8,
        "ft.com": 8,
        "wsj.com": 8,
        "nytimes.com": 8,
        "theguardian.com": 7,
        "apple.com": 10,
        "openai.com": 10,
        "travel.state.gov": 10,
        "state.gov": 10,
        "uscis.gov": 10,
        "fifa.com": 10,
    }

    OUTDATED_YEARS = [
        "2020",
        "2021",
        "2022",
        "2023",
        "2024"
    ]

    def get_domain(self, url: str) -> str:
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.replace("www.", "")
            return domain
        except Exception:
            return ""

    def score_source(self, url: str) -> int:
        domain = self.get_domain(url)

        for trusted_domain, score in self.HIGH_QUALITY_DOMAINS.items():
            if trusted_domain in domain:
                return score

        return 3

    def is_outdated(self, title: str, body: str) -> bool:
        text = f"{title} {body}"

        for year in self.OUTDATED_YEARS:
            if year in text:
                return True

        return False

    def filter_results(self, results: list, max_results: int = 5) -> list:
        filtered = []

        for item in results:
            title = item.get("title", "")
            body = item.get("body", "")
            url = item.get("href", "")

            if self.is_outdated(title, body):
                continue

            score = self.score_source(url)

            filtered.append({
                "title": title,
                "body": body,
                "url": url,
                "score": score
            })

        filtered.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return filtered[:max_results]
