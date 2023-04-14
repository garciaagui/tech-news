import sys

from .scraper import get_tech_news

from .analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)

from .analyzer.ratings import top_5_categories

# def print_menu():
#     menu_options = {
#         0: "0 - Popular o banco com notícias;\n",
#         1: "1 - Buscar notícias por título;\n",
#         2: "2 - Buscar notícias por data;\n",
#         3: "3 - Buscar notícias por categoria;\n",
#         4: "4 - Listar top 5 categorias;\n",
#         5: "5 - Sair.\n",
#     }

#     print("Selecione uma das opções a seguir:\n")
#     for key in menu_options.keys():
#         print(menu_options[key])


def initialize_get_tech_news():
    amount = int(input("Digite quantas notícias serão buscadas: "))
    get_tech_news(amount)


def initialize_search_by_title():
    title = str(input("Digite o título: "))
    return search_by_title(title)


def initialize_search_by_date():
    date = str(input("Digite a data no formato aaaa-mm-dd: "))
    return search_by_date(date)


def initialize_search_by_category():
    category = str(input("Digite a categoria: "))
    return search_by_category(category)


def initialize_top_5_categories():
    return top_5_categories()


def exit():
    return "Encerrando script"


def get_function_by_option(option: int):
    func_options = {
        0: initialize_get_tech_news,
        1: initialize_search_by_title,
        2: initialize_search_by_date,
        3: initialize_search_by_category,
        4: initialize_top_5_categories,
        5: exit,
    }

    if option not in func_options:
        raise KeyError()

    else:
        print(func_options[option]())


def analyzer_menu():

    # print_menu()

    print(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n "
        "4 - Listar top 5 categorias;\n 5 - Sair."
    )

    try:
        selected_option = int(input())
        get_function_by_option(selected_option)

    except (ValueError, KeyError):
        sys.stderr.write("Opção inválida\n")
