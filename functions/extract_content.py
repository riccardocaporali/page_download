import requests
from bs4 import BeautifulSoup

def extract_content(url: str):
    """Downloads a webpage and extracts all h1, h2, and p texts in DOM order."""
    try:
        # Fetch HTML content from the given URL
        resp = requests.get(url, timeout=10)
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