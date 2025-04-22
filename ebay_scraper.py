# ebay_scraper.py
#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def scrape_ebay(query):
    """
    Fetches the first page of eBay search results for the given query
    and returns a list of (title, price) tuples.
    """
    url = f"https://www.ebay.com/sch/i.html?_nkw={quote_plus(query)}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    items = soup.select("li.s-item")

    results = []
    for item in items:
        # Extract title
        t = item.select_one(".s-item__title span[role='heading']")
        # Extract price
        p = item.select_one(".s-item__price")
        if not t or not p:
            continue
        title = t.get_text(strip=True)
        price = p.get_text(strip=True)
        results.append((title, price))

    # Remove the first two placeholder entries
    return results[2:] if len(results) > 2 else []
