import os
from functions.search_google import search_google
from functions.extract_content import extract_content

# Search parameters
query = "arredamento design torino"
num_results = 10
language = "it" #"it"
country = "it" #"it"
domain = "google.it" #"google.it"

# Search result and extract urls
items = search_google(query, num_results=num_results, language=language, country=country)
urls = [item["link"] for item in items]

# Extract content from site
results = []
for url in urls:
    data = extract_content(url)  
    if data:
        results.append({"url": url, "content": data})

# Test search
if items:
    for i, item in enumerate(items[:10], start=1):
        print(f"{i}. {item['link']}")
else:
    print("No result found")

# Test extract data
page_number = 0 # The first is 0
entries = 1
if not results:
    print("No extractable content found.")
else:
    page = results[page_number]  # Show first site
    content = page.get("content", [])

    if not content:
        print("No readable content found.")
    else:
        print(f"\nExtracted content from: {page['url']}\n")
        for block in content[:entries]:  # show first 20 entries
            print(f"[{block['tag'].upper()}] {block['text']}")