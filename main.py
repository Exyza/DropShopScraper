# main.py
#!/usr/bin/env python3

import sys
from ebay_scraper import scrape_ebay


def main():
    if sys.stdin.isatty() and len(sys.argv) < 2:
        print("Usage: python main.py \"search term\"")
        sys.exit(1)

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = sys.stdin.read().strip()

    results = scrape_ebay(query)
    for title, price in results:
        print(f"{price} — {title}")


if __name__ == "__main__":
    main()
