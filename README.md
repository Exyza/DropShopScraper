# DropShopScraper
---
This is the prototype code that will eventually be used for the backend Web Application that runs DropShop.
Currently (04/21/2025), there is only one scraper up and running (that being one working for ebay).
It is VERY simple, and will need continuted work to set it in line with the vision of dropshop.
---
Further edits for the ebay scraper include:
- (COMPLETED 04/22/2025) Adding better parsing functions in order to remove data unrelated to search queries
- Performing necessary data transformaitons so that this data can be used in a back-end SQL database
- (ADDED SOME FUNCTIONALITY 04/22/2025) Add better parsing functions to accurately represent all queries
---
Further edits for the scraper overall:
- Adding functionality such that front-end user searches are uses for Web Application queries
- Adding functionality so that any further website parsers provide accurate data related to the search
- Fixing the major bug in aliexpress_scraper.py's inability to properly mine out product title and price data
---
***THIS IS A WORK IN PROGRESS***
---
Edit for 04/22/2025
So far, the ebay parser does it's job pretty well.
When used, it will pull data from the default ebay query.
This means it will pull AROUND 60-70 enteries per product search.
