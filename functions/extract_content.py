import requests
from bs4 import BeautifulSoup
import time

def extract_content(url: str, retries=3, timeout=10):
    """Downloads a webpage and extracts h1, h2, h3, p, li, and text-bearing divs in DOM order."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    # Retry loop
    for _ in range(retries):
        try:
            resp = requests.get(url, headers=headers, timeout=timeout)
            resp.raise_for_status()
            break
        except requests.RequestException:
            time.sleep(1)
    else:
        print(f"Error fetching {url}")
        return None

    # CONTENT-TYPE CHECK → skip non-HTML (PDF, images, etc.)
    content_type = resp.headers.get("Content-Type", "").lower()
    if "text/html" not in content_type:
        print(f"Skipping non-HTML content: {url} ({content_type})")
        return None

    # Encoding + parser
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, "html.parser")

    tags = ["h1", "h2", "h3", "p"]

    content = []
    for tag in soup.find_all(tags):
        text = tag.get_text(strip=True)

        # Skip empty divs
        if tag.name == "div" and not text:
            continue

        # Skip tiny garbage
        if len(text) < 3:
            continue

        content.append({"tag": tag.name, "text": text})

    return content if content else None