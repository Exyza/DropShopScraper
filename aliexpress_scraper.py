# aliexpress_scraper.py
#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def scrape_aliexpress(query):
    """
    Fetches the first page of AliExpress search results for the given query
    and returns a list of (title, price) tuples.
    """
    # encode spaces as %20 for AliExpress URL
    url = f"https://www.aliexpress.us/wholesale?SearchText={quote(query)}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    results = []

    # select all product card links
    cards = soup.select("a.search-card-item")
    for card in cards:
        # first try to get the title from the div.l0_ag title attribute
        title_el = card.find("div", class_="l0_ag")
        if title_el and title_el.has_attr("title") and title_el["title"].strip():
            title = title_el["title"].strip()
        else:
            # fallback to the visible <h3> text
            h3 = card.find("h3", class_="l0_j0")
            title = h3.get_text(strip=True) if h3 else None
        if not title:
            continue

        # extract price spans from container with class 'l0_k1'
        price_container = card.find("div", class_="l0_k1")
        if not price_container:
            continue
        spans = price_container.find_all("span")
        price = ''.join(span.get_text(strip=True) for span in spans)

        results.append((title, price))

    return results
