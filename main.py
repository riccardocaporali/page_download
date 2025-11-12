import os
from functions.search_google import search_google
from functions.extract_content import extract_content

# Search parameters
query = "site:nasa.gov filetype:html" #Search key
num_results = 10 # Number of pages
start = 1 # Starting page

# Search result and extract urls
items = search_google(query, num_results, start)
urls = [item["link"] for item in items]

# Extract content from site
results = []
for url in urls:
    data = extract_content(url)  
    if data:
        results.append({"url": url, "content": data})

"""# Test search
if items:
    for i, item in enumerate(items[:10], start=1):
        print(f"{i}. {item['link']}")
else:
    print("No result found")"""

# Test extract data
page_number = 3
entries = 5
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