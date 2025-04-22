# ebay_scraper.py                                                                                                                                                                             
#!/usr/bin/env python3                                                                                                                                                                        
                                                                                                                                                                                              
import re                                                                                                                                                                                     
import requests                                                                                                                                                                               
from bs4 import BeautifulSoup, SoupStrainer                                                                                                                                                   
from urllib.parse import quote_plus                                                                                                                                                           
                                                                                                                                                                                              
                                                                                                                                                                                              
def scrape_ebay(query):                                                                                                                                                                       
    """                                                                                                                                                                                       
    Fetches eBay search results for `query`, extracts titles and prices,                                                                                                                      
    and returns a list of (title, price) tuples in the order they appear.                                                                                                                     
                                                                                                                                                                                              
    Post-processing removes duplicate listings and skips any "Shop on eBay"                                                                                                                   
    placeholders, and strips literal "New Listing" from titles.                                                                                                                               
    """                                                                                                                                                                                       
    url = f"https://www.ebay.com/sch/i.html?_nkw={quote_plus(query)}"                                                                                                                         
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}                                                                                                                     
    response = requests.get(url, headers=headers)                                                                                                                                             
    response.raise_for_status()                                                                                                                                                               
                                                                                                                                                                                              
    # Only parse <li> items with data-marko-key                                                                                                                                               
    strainer = SoupStrainer(                                                                                                                                                                  
        "li",                                                                                                                                                                                 
        attrs={"data-marko-key": re.compile(r".+")}                                                                                                                                           
    )                                                                                                                                                                                         
    soup = BeautifulSoup(response.text, "html.parser", parse_only=strainer)

    raw_results = []
    for li in soup.find_all("li", attrs={"data-marko-key": True}):
        info = li.select_one("div.s-item__info.clearfix")
        if not info:
            continue
        title_tag = info.select_one(".s-item__title span[role='heading']")
        price_tag = info.select_one(".s-item__price")
        if not title_tag or not price_tag:
            continue
        title = title_tag.get_text(strip=True)
        price = price_tag.get_text(strip=True)
        raw_results.append((title, price))

    final_results = []
    seen = set()
    for title, price in raw_results:
        low = title.strip().lower()
        if low.startswith("shop on ebay"):
            continue
        key = (title, price)
        if key in seen:
            continue
        seen.add(key)
        # Remove any "New Listing" text from title
        clean_title = re.sub(r"(?i)new listing", "", title).strip()
        final_results.append((clean_title, price))

    return final_results
