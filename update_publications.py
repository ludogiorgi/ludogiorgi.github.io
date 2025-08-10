"""Fetch publications from Google Scholar and write them to an HTML file."""

from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

USER_ID = "DA5vUj0AAAAJ"
OUTPUT_FILE = Path("publications.html")
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    )
}


def fetch_publications(user_id: str) -> list[str]:
    """Return a list of formatted publication strings for the given user."""

    base = (
        f"https://scholar.google.com/citations?user={user_id}&hl=en"
        "&view_op=list_works&sortby=pubdate"
    )
    start = 0
    pubs: list[str] = []
    while True:
        url = f"{base}&cstart={start}&pagesize=100"
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        rows = soup.select("tr.gsc_a_tr")
        added = False
        for row in rows:
            title_tag = row.select_one("a.gsc_a_at")
            if title_tag is None:
                continue
            title = title_tag.text.strip()
            link = urljoin("https://scholar.google.com", title_tag["href"])
            authors = row.select("div.gs_gray")[0].text
            info_div = row.select("div.gs_gray")[1]
            info_text = info_div.text
            year_tag = row.select_one("span.gs_oph")
            year = year_tag.text.strip().strip(", ") if year_tag else ""
            venue = info_text.replace(f", {year}", "") if year else info_text
            item = (
                f"{authors}, <em>{title}</em>, "
                f"<a href=\"{link}\" target=\"_blank\">{venue} ({year})</a>."
            )
            pubs.append(item)
            added = True
        if not added:
            break
        start += 100
    return pubs


def main() -> None:
    pubs = fetch_publications(USER_ID)
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        for item in pubs:
            f.write(f"<li>{item}</li>\n")


if __name__ == "__main__":
    main()

