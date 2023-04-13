import requests
import time
from bs4 import BeautifulSoup


def fetch(url):
    TIMEOUT_SECONDS = 3
    HEADERS = {"user-agent": "Fake user-agent"}
    RATE_LIMIT_SECONDS = 1

    try:
        response = requests.get(
            url,
            timeout=TIMEOUT_SECONDS,
            headers=HEADERS,
        )
        response.raise_for_status()
        time.sleep(RATE_LIMIT_SECONDS)

    except (requests.HTTPError, requests.ReadTimeout):
        return None

    else:
        return response.text


def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    headers = soup.find_all("h2", {"class": "entry-title"})
    news_urls = list()

    for header in headers:
        url = header.find("a")["href"]
        news_urls.append(url)

    return news_urls


def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page_link = soup.find("a", {"class": "next page-numbers"})

    if not next_page_link:
        return None

    return next_page_link["href"]


# html = fetch("https://blog.betrybe.com")
# print(scrape_next_page_link(html))


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
