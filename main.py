# main.py
#!/usr/bin/env python3
import argparse
from ebay_scraper import scrape_ebay
from aliexpress_scraper import scrape_aliexpress

def main():
    parser = argparse.ArgumentParser(
        description="Run both eBay and AliExpress scrapers for a given query."
    )
    parser.add_argument(
        "query", nargs="?", help="Search query (in quotes if multi-word)."
    )
    args = parser.parse_args()

    search = args.query if args.query else input("Enter search term: ")

    # eBay results
    print(f"\n=== eBay Results for '{search}' ===")
    ebay_listings = scrape_ebay(search)
    if not ebay_listings:
        print("No eBay items found.")
    else:
        for idx, (title, price) in enumerate(ebay_listings, start=1):
            print(f"{idx}. {title} — {price}")

    # AliExpress results
    print(f"\n=== AliExpress Results for '{search}' ===")
    ali_listings = scrape_aliexpress(search)
    if not ali_listings:
        print("No AliExpress items found.")
    else:
        for idx, (title, price) in enumerate(ali_listings, start=1):
            print(f"{idx}. {title} — {price}")

if __name__ == "__main__":
    main()
  
