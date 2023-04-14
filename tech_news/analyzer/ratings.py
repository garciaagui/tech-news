from ..database import find_news
from .search_engine import search_by_category


def get_categories():
    categories = set()

    for news in find_news():
        categories.add(news["category"])

    return categories


def top_5_categories():
    categories = get_categories()
    ratings = list()

    for category in categories:
        category_counter = tuple((category, len(search_by_category(category))))
        ratings.append(category_counter)

    ratings.sort(key=lambda a: (-a[1], a[0]))
    # -a[1] -> 1o criteria - Sort category counter in descending order
    # a[0] -> 2o criteria - Sort category name in ascending order

    return [rating[0] for rating in ratings[:5]]
