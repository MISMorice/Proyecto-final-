import requests
from bs4 import BeautifulSoup

def scrape_example():
    url = "http://example.com"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    sp = BeautifulSoup(response.text, "html.parser")

    title_element = sp.find("h1")

    title = (
        title_element.get_text(strip=True)
            if title_element
            else "Sin título"
    )

    return {
        "title": title,
        "url": url
    }

if __name__ == "__main__":
    result = scrape_example()
    print(result)