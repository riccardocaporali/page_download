# main.py
from pathlib import Path
from src.crawler import run_query, save_results

# Search parameters
query = "arredamento design torino"
num_results = 3
language = "it"
country = "it"
domain = "google.it"

# ---- CORE EXECUTION ----
results = run_query(
    query,
    num_results=num_results,
    language=language,
    country=country,
    domain=domain,
)
print("Num results:", len(results))

# ---- SAVE RESULTS ----
# Simple slug for folder name
folder_name = query.replace(" ", "_")
out_dir = Path("output") / folder_name
save_results(results, out_dir)

# ---- TEST SEARCH (same as original) ----
if results:
    print("Top URLs:")
    for i, page in enumerate(results[:10], start=1):
        print(f"{i}. {page['url']}")
else:
    print("No result found")

# ---- TEST EXTRACT DATA ----
page_number = 1
entries = 10

if not results:
    print("No extractable content found.")
elif page_number >= len(results):
    print(f"Page {page_number} out of range (only {len(results)} available).")
else:
    page = results[page_number]
    content = page.get("content", [])

    if not content:
        print("No readable content found.")
    else:
        print(f"\nExtracted content from: {page['url']}\n")
        for block in content[:entries]:
            print(f"[{block['tag'].upper()}] {block['text']}")