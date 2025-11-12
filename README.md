# Page Download

Python toolset for automated web search and content extraction using the **Google Custom Search API**.

## Overview
This project performs automated searches on Google through the Custom Search API, retrieves the result URLs, and extracts readable content (`h1`, `h2`, `p`) from each webpage.

## Features
- Google Custom Search integration (official API)
- Environment-based configuration (`.env`)
- Extraction of semantic HTML elements
- JSON-ready structured output for text analysis
- Modular, minimal design (`functions/` + `main.py`)

## Structure
```text
page_download/
├── functions/
│   ├── search_google.py
│   ├── extract_content.py
├── main.py
├── .env
└── README.md
```

## Setup
# 1. Install dependencies
uv pip install google-api-python-client python-dotenv beautifulsoup4 requests
ini

# 2. Create .env
GCP_CSE_API_KEY=your_api_key
GCP_CSE_CX=your_custom_search_engine_id
bash

# 3. Run the main script
uv run python main.py

## Example output
Extracted content from: https://carbon.nasa.gov/app_readiness.html

[H1] National Aeronautics and Space Administration
[H2] CMS Project Application Readiness Levels
[P] Start Year 2018 CMS Projects
...

## Notes
Google Custom Search API returns a maximum of 100 results (10 per page).
Non-HTML files (PDF, images, etc.) are skipped automatically.

## License
MIT License