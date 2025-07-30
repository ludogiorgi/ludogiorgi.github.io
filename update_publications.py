import json
from pathlib import Path
from scholarly import scholarly

USER_ID = "DA5vUj0AAAAJ"
OUTPUT_FILE = Path("publications.html")


def fetch_publications(user_id):
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["publications"])
    pubs = []
    for pub in author.get("publications", []):
        filled = scholarly.fill(pub)
        bib = filled.get("bib", {})
        title = bib.get("title", "")
        authors = bib.get("author", "")
        year = bib.get("pub_year", "")
        venue = bib.get("venue", "")
        url = filled.get("pub_url", "")
        item = (
            f"{authors}, <em>{title}</em>, "
            f"<a href=\"{url}\" target=\"_blank\">{venue} ({year})</a>."
        )
        pubs.append(item)
    return pubs


def main():
    pubs = fetch_publications(USER_ID)
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        for item in pubs:
            f.write(f"<li>{item}</li>\n")


if __name__ == "__main__":
    main()
