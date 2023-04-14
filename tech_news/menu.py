import sys


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


def get_function_by_selected_option(option: int):
    func_options = {
        0: "Digite quantas notícias serão buscadas:",
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a categoria:",
        4: "Listando top 5 categorias...",
        5: "Saindo...",
    }

    if option not in func_options:
        raise KeyError()

    else:
        print(func_options[option])


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
        get_function_by_selected_option(selected_option)

    except (ValueError, KeyError):
        sys.stderr.write("Opção inválida")
