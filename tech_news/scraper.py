import requests
import time
from bs4 import BeautifulSoup
import re


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


def get_only_time(reading_time: str):
    number_extracted = re.sub("\D", "", reading_time)
    return int(number_extracted)


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    url = soup.find("div", {"class": "pk-share-buttons-wrap"})[
        "data-share-url"
    ]
    title = (soup.find("h1", {"class": "entry-title"}).text).strip()
    timestamp = soup.find("li", {"class": "meta-date"}).text
    writer = soup.find("span", {"class": "author"}).text
    reading_time = get_only_time(
        soup.find("li", {"class": "meta-reading-time"}).text
    )
    summary = (soup.find("div", {"class": "entry-content"}).p.text).strip()
    category = (
        soup.find("a", {"class": "category-style"})
        .find("span", {"class": "label"})
        .text
    )

    return dict(
        url=url,
        title=title,
        timestamp=timestamp,
        writer=writer,
        reading_time=reading_time,
        summary=summary,
        category=category,
    )


html = fetch("https://blog.betrybe.com/tecnologia/cabos-de-rede/")
print(scrape_news(html))


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
