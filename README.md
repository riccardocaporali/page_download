# Page Download

Python toolset for automated web search and content extraction using SerpAPI.

## Overview
This project performs automated Google searches through SerpAPI, retrieves organic result URLs, and extracts readable content (h1, h2, p) from each webpage.

## Features
- SerpAPI integration for real organic Google results
- Environment-based configuration (`.env`)
- Extraction of semantic HTML elements
- JSON-ready structured output for text analysis
- Modular, minimal design (`functions/` + `main.py`)

## Structure
```text
page_download/
├── main.py
├── README.md
├── pyproject.toml
├── output/
│   └── ...
└── src/
    ├── crawler/
    │   ├── __init__.py
    │   ├── search_google.py
    │   ├── run_query.py
    │   ├── extract_content.py
    │   └── save_results.py
    ├── utils/
    │   ├── __init__.py
    │   ├── create_snapshot.py
    │   └── get_project_root.py
    └── agent/
```

## Setup
# 1. Install dependencies
uv pip install google-search-results python-dotenv beautifulsoup4 requests
ini

# 2. Create .env
SERPAPI_KEY=your_api_key

# 3. Run the main script
uv run python main.py

## Example output
Extracted content from: https://carbon.nasa.gov/app_readiness.html

[H1] National Aeronautics and Space Administration
[H2] CMS Project Application Readiness Levels
[P] Start Year 2018 CMS Projects
...

## Notes
SerpAPI returns organic Google results with rich metadata.
Non-HTML files (PDF, images, etc.) are skipped automatically.

## License
MIT License