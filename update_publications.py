"""Fetch publications from Google Scholar via SerpAPI and write them to an HTML file."""

from __future__ import annotations

import os
from pathlib import Path
import requests

USER_ID = "DA5vUj0AAAAJ"
OUTPUT_FILE = Path("publications.html")
API_URL = "https://serpapi.com/search.json"


def fetch_publications(user_id: str, api_key: str) -> list[str]:
    """Return a list of formatted publication strings for the given user."""
    start = 0
    pubs: list[str] = []
    while True:
        params = {
            "engine": "google_scholar_author",
            "author_id": user_id,
            "sort_by": "pubdate",
            "num": 100,
            "start": start,
            "api_key": api_key,
        }
        resp = requests.get(API_URL, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        articles = data.get("articles", [])
        if not articles:
            break
        for art in articles:
            title = art.get("title", "").strip()
            link = art.get("link", "")
            authors = art.get("authors", "")
            venue = art.get("publication", "")
            year = art.get("year", "")
            item = (
                f"{authors}, <em>{title}</em>, "
                f"<a href=\"{link}\" target=\"_blank\">{venue} ({year})</a>."
            )
            pubs.append(item)
        if not data.get("next"):
            break
        start += 100
    return pubs


def main() -> None:
    api_key = os.environ.get("SERPAPI_API_KEY")
    if not api_key:
        raise RuntimeError("SERPAPI_API_KEY environment variable not set")
    pubs = fetch_publications(USER_ID, api_key)
    OUTPUT_FILE.write_text(
        "\n".join(f"<li>{p}</li>" for p in pubs),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
