import requests
from bs4 import BeautifulSoup

def extract_content(url: str):
    """Downloads a webpage and extracts all h1, h2, and p texts in DOM order."""
    try:
        # Add a browser-like User-Agent to avoid 403 errors
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        # Handle connection, timeout, or HTTP errors
        print(f"Error fetching {url}: {e}")
        return None

    # Ensure correct text encoding
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, "html.parser")

    content = []
    # Iterate through tags in the order they appear in the DOM
    for tag in soup.find_all(["h1", "h2", "p"]):
        text = tag.get_text(strip=True)
        if text:
            content.append({"tag": tag.name, "text": text})

    # Return structured content or None if page is empty
    return content if content else None