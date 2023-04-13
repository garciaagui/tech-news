import requests
import time
from bs4 import BeautifulSoup
import re
from .database import create_news


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


def get_url(soup) -> str:
    link_element = soup.find("div", {"class": "pk-share-buttons-wrap"})
    return link_element["data-share-url"]


def get_title(soup) -> str:
    title_content = soup.find("h1", {"class": "entry-title"}).text
    return title_content.strip()


def get_timestamp(soup) -> str:
    return soup.find("li", {"class": "meta-date"}).text


def get_writer(soup) -> str:
    return soup.find("span", {"class": "author"}).text


def get_reading_time(soup) -> int:
    reading_time_element = soup.find("li", {"class": "meta-reading-time"}).text
    number_extracted = re.sub("\D", "", reading_time_element)
    return int(number_extracted)


def get_summary(soup) -> str:
    summary_content = soup.find("div", {"class": "entry-content"}).p.text
    return summary_content.strip()


def get_category(soup) -> str:
    category_element = soup.find("a", {"class": "category-style"})

    return category_element.find("span", {"class": "label"}).text


def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    return dict(
        url=get_url(soup),
        title=get_title(soup),
        timestamp=get_timestamp(soup),
        writer=get_writer(soup),
        reading_time=get_reading_time(soup),
        summary=get_summary(soup),
        category=get_category(soup),
    )


def define_range(amount, counter, news_length):
    sum = counter + news_length

    if sum > amount:
        range = news_length - (sum - amount)
    else:
        range = news_length

    return range


def get_tech_news(amount):
    current_url = "https://blog.betrybe.com/"
    news_to_insert = list()
    counter = 0

    while counter < amount:
        main_page_html_content = fetch(current_url)
        news_urls = scrape_updates(main_page_html_content)
        range = define_range(amount, counter, len(news_urls))

        for url in news_urls[:(range)]:
            news_page_html_content = fetch(url)
            news_to_insert.append(scrape_news(news_page_html_content))

        counter += range
        current_url = scrape_next_page_link(main_page_html_content)
        if not current_url:
            break

    create_news(news_to_insert)
    return news_to_insert
