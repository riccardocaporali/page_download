import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

def search_google(query, num_results=10, start=1, language="lang_it", country="countryIT"):
    """Execute Google Custom Search with specified input"""
    load_dotenv()
    api_key = os.environ["GCP_CSE_API_KEY"]
    cx = os.environ["GCP_CSE_CX"]

    service = build("customsearch", "v1", developerKey=api_key)

    res = service.cse().list(
        q=query,
        cx=cx,
        num=num_results,
        start=start,
        lr=language,
        cr=country
    ).execute()

    items = res.get("items", [])
    return items if items else None