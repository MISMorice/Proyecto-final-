from app.scrapers.example_scraper import scrape_example
from app.database import save_item

def run_scraper():
    item = scrape_example()

    save_item(
        item["title"],
        item["url"]
    )

    return item