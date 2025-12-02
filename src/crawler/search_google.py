import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

def search_google(query, engine="google", num_results=10, language=None, country=None, domain=None):
    """Esegue ricerca Google tramite SerpAPI"""
    load_dotenv()
    api_key = os.environ["SERPAPI_KEY"]

    params = {
        "engine": engine,
        "q": query,
        "api_key": api_key,
        "num": num_results,
        "hl": language,       
        "gl": country,         
        "google_domain": domain  
    }

    results = GoogleSearch(params).get_dict()
    return results.get("organic_results", None)