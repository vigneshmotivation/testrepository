"""
Run this script in VS Code.

USAGE:
1. Put your HTML snippet into a text file, example: input.html
2. Run this script:
      python extract_me_urls.py
3. Output will be written: output.csv
"""

import csv
from pathlib import Path
from bs4 import BeautifulSoup


# ---- Configure your prefix here ----
BASE_PREFIX = "https://www.manageengine.com/products/applications_manager/help/"


def extract_links_and_parents(html_source: str):
    soup = BeautifulSoup(html_source, "html.parser")
    results = []

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()

        if not href.endswith(".html"):  # skip non-html
            continue

        # prefix target
        full_url = BASE_PREFIX + href.lstrip("/")

        # walk up looking for <span> text
        hierarchy = []
        parent = a.parent

        while parent:
            if parent.name == "span":
                text = parent.get_text(strip=True)
                if text and text not in hierarchy:
                    hierarchy.append(text)
            parent = parent.parent

        hierarchy.reverse()

        results.append((full_url, " > ".join(hierarchy)))

    return results


def main():
    input_file = Path("/Users/vignesh-20727/Desktop/pyprojs/urlmanipulator/urls.html")
    if not input_file.exists():
        print("❌ input.html not found. Please create it in the same folder.")
        return

    html = input_file.read_text(encoding="utf-8", errors="ignore")

    rows = extract_links_and_parents(html)

    # write CSV
    output_file = Path("output.csv")
    with output_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["url", "hierarchy"])
        writer.writerows(rows)

    print(f"✔ Done! Extracted {len(rows)} URLs.")
    print(f"➡ CSV written to: {output_file.resolve()}")


if __name__ == "__main__":
    main()
