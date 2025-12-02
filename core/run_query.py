# core/run_query.py
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

from functions.search_google import search_google
from functions.extract_content import extract_content


def run_query(
    query: str,
    *,
    num_results: int = 10,
    language: str = None,
    country: str = None,
    domain: str = None,
) -> list[dict]:
    """Search → extract URLs → download pages → parse content using SerpAPI."""

    load_dotenv()

    # --- 1. Perform SerpAPI search ---
    items = search_google(
        query,
        num_results=num_results,
        language=language,
        country=country,
        domain=domain,
    )

    if not items:
        return []

    urls = [item["link"] for item in items]

    results = []

    # --- 2. Extract content from each page ---
    for url in urls:
        try:
            blocks = extract_content(url)

            # Fallback: extract page title
            try:
                r = requests.get(url, timeout=10)
                soup = BeautifulSoup(r.text, "html.parser")
                title = soup.title.string.strip() if soup.title else None
            except:
                title = None

            if not blocks:
                results.append({
                    "url": url,
                    "status": "empty",
                    "title": title,
                    "content": []
                })
                continue

            results.append({
                "url": url,
                "status": "ok",
                "title": title,
                "content": blocks
            })

        except Exception as e:
            results.append({
                "url": url,
                "status": "error",
                "error": str(e),
                "title": None,
                "content": []
            })

    return results