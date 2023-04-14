from ..database import search_news


def search_by_title(title: str):
    found_news = list()
    query = {"title": {"$regex": title.lower()}}

    for news in search_news(query):
        found_news.append((news["title"], news["url"]))

    return found_news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
