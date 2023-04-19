from ..database import search_news

from datetime import datetime
import re


def search_by_title(title: str):
    found_news = list()
    query = {"title": {"$regex": title.lower()}}

    for news in search_news(query):
        found_news.append((news["title"], news["url"]))

    return found_news


def convert_date(date):
    DATE_REGEX = r"\d{4}-\d{2}-\d{2}"

    try:
        if re.match(DATE_REGEX, date):
            return datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        else:
            raise Exception

    except Exception:
        raise ValueError("Error: Invalid date")


def search_by_date(date):
    found_news = list()
    converted_date = convert_date(date)

    query = {"timestamp": converted_date}

    for news in search_news(query):
        found_news.append((news["title"], news["url"]))

    return found_news


def search_by_category(category: str):
    CATEGORY_REGEX = re.compile(category, re.IGNORECASE)

    found_news = list()
    query = {"category": {"$regex": CATEGORY_REGEX}}

    for news in search_news(query):
        found_news.append((news["title"], news["url"]))

    return found_news
