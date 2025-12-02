# core/save_results.py
import json
from pathlib import Path


def save_results(results: list[dict], out_dir: Path) -> None:
    """Save each result into a numbered JSON file inside out_dir/."""

    # Create output directory if it does not exist
    out_dir.mkdir(parents=True, exist_ok=True)

    # Save each page as a separate JSON file
    for idx, page in enumerate(results, start=1):
        file_path = out_dir / f"{idx:03d}_page.json"

        with file_path.open("w", encoding="utf-8") as f:
            json.dump(
                page,
                f,
                indent=2,
                ensure_ascii=False
            )