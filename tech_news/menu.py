import sys

from .scraper import get_tech_news

from .analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)

from .analyzer.ratings import get_top_5_categories


def print_menu():
    menu_options = {
        0: "0 - Populate the bank with news;",
        1: "1 - Search news by title;",
        2: "2 - Search news by date;",
        3: "3 - Search news by category;",
        4: "4 - List top 5 categories;",
        5: "5 - Exit.\n",
    }

    print("Select one of the following options:")
    for key in menu_options.keys():
        print(menu_options[key])


def initialize_get_tech_news():
    amount = int(input("Enter how many news to search for: "))
    get_tech_news(amount)


def initialize_search_by_title():
    title = str(input("Enter title: "))
    return search_by_title(title)


def initialize_search_by_date():
    date = str(input("Enter date in 'yyyy-mm-dd' format: "))
    return search_by_date(date)


def initialize_search_by_category():
    category = str(input("Enter the category: "))
    return search_by_category(category)


def initialize_get_top_5_categories():
    return get_top_5_categories()


def exit():
    return "Closing script..."


def get_function_by_option(option: int):
    func_options = {
        0: initialize_get_tech_news,
        1: initialize_search_by_title,
        2: initialize_search_by_date,
        3: initialize_search_by_category,
        4: initialize_get_top_5_categories,
        5: exit,
    }
    try:
        print(func_options[option]())

    except KeyError:
        raise ValueError("Invalid option")


def input_select_option():
    try:
        selected_option = int(input("Selected option: "))

    except ValueError:
        raise ValueError("Invalid option")

    else:
        return selected_option


def analyzer_menu():
    print_menu()

    try:
        selected_option = input_select_option()
        get_function_by_option(selected_option)

    except Exception as e:
        sys.stderr.write(f"{e}\n")
