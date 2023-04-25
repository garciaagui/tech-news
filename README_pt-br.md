<a name="readme-top"></a>

<h1 align="center">Tech News 📰</h1>

> [🇺🇸 Click here to access the English version.](README.md)

## Sumário

<ol>
  <li><a href="#sobre-o-projeto">Sobre o Projeto</a></li>
  <li><a href="#tecnologias">Tecnologias</a></li>
  <li><a href="#funcionalidades">Funcionalidades</a></li>
  <li><a href="#como-executar-o-projeto">Como Executar o Projeto</a></li>
  <li><a href="#sobre-a-trybe">Sobre a Trybe</a></li>
  <li><a href="#contato">Contato</a></li>
</ol>

## Sobre o Projeto

Projeto **31** do curso de Desenvolvimento Web da [Trybe][trybe-site-url].

Tech News é um projeto em [Python][python-url] que utiliza [Beautiful Soup][bs4-url] para fazer raspagem de dados no [blog da Trybe][trybe-blog-url], coletando notícias e artigos sobre tecnologia e armazenando-os em um banco de dados [MongoDB][mongodb-url].

> ℹ️ Escrevi testes para as funções implementadas pelo Trybe. Esses testes podem ser encontrados no subdiretório de `tests`.

<br/>

## Tecnologias

O projeto foi desenvolvido em [Python][python-url] e testado com [Pytest][pytest-url]. O banco de dados utilizado foi o [MongoDB][mongodb-url], e a conexão e interação com ele foram estabelecidas através da biblioteca [PyMongo][pymongo-url]. Para garantir a qualidade do código, utilizou-se o [Flake8][flake8-url], e a raspagem de dados na web foi realizada com o [Beautiful Soup][bs4-url].

[![Python][python-badge]][python-url] [![MongoDB][mongodb-badge]][mongodb-url] [![PyMongo][pymongo-badge]][pymongo-url] [![Beautiful Soup][bs4-badge]][bs4-url] [![Pytest][pytest-badge]][pytest-url] [![Flake8][flake8-badge]][flake8-url]

<br/>

## Funcionalidades

<ul>
  <li>Coletar notícias e artigos do blog da Trybe usando raspagem de dados e armazená-los em um banco de dados MongoDB.</li>
  <li>Pesquisar notícias por título.</li>
  <li>Pesquisar notícias por data.</li>
  <li>Pesquisar notícias por categoria.</li>
  <li>Listar as 5 categorias com mais notícias.</li>
</ul>

<br/>

## Como Executar o Projeto

Para rodar o projeto localmente, siga os passos abaixo.

1. Clone o repositório.

```
git clone git@github.com:garciaagui/tech-news.git
```

2. Navegue até a raiz do projeto.

```
cd tech-news/
```

3. Crie o ambiente virtual.

```
python3 -m venv .venv
```

4. Ative o ambiente virtual.

```
source .venv/bin/activate
```

-   Note que no começo da linha do terminal haverá `(.venv)`, como no exemplo abaixo.

```
(.venv) gui@gui-desktop:~/Trybe/tech-news$
```

-   Para desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativá-lo novamente quando retornar ao projeto.

5. Instale as dependências no ambiente virtual.

```
python3 -m pip install -r dev-requirements.txt
```

6. Se você não tiver o MongoDB instalado localmente, inicie-o via Docker.

```
docker-compose up -d mongodb
```

-   ℹ️ O nome do banco de dados é `tech_news`.

7. Por fim, execute o seguinte comando para acessar o menu.

```
tech-news-analyzer
```

<details>
  <summary><strong> ℹ️ Para instruções adicionais, clique aqui.</strong></summary><br />

-   🧪 Para rodar **todos** os testes, execute o comando abaixo.

```
python3 -m pytest
```

-   🧪 Para rodar apenas um arquivo de teste, siga o exemplo abaixo.

```
python3 -m pytest tests/reading_plan/test_reading_plan.py
```

-   🧪 Para rodar apenas um teste específico, siga o exemplo abaixo.

```
python3 -m pytest -k test_reading_plan_group_news_with_valid_input
```

-   Caso deseje fazer testes manuais diretamente nos módulos onde as funções foram implementadas, siga o exemplo abaixo.

```
python3 -m tech_news.scraper.py
```

</details>

<br/>

## Sobre a Trybe

_"A [Trybe][trybe-site-url] é uma escola do futuro para qualquer pessoa que queira melhorar de vida e construir uma carreira de sucesso em tecnologia, onde a pessoa só paga quando conseguir um bom trabalho."_

_"O programa conta com mais de 1.500 horas de aulas online, aborda introdução ao desenvolvimento de software, front-end, back-end, ciência da computação, engenharia de software, metodologias ágeis e habilidades comportamentais._"

<br/>

## Contato

Projeto desenvolvido por **Guilherme Garcia**. Seguem abaixo minhas redes sociais e meios de contato. 🤘

[![Gmail][gmail-badge]][gmail-url]
[![Linkedin][linkedin-badge]][linkedin-url]
[![GitHub][github-badge]][github-url]
[![Instagram][instagram-badge]][instagram-url]

<p align="right"><a href="#readme-top">Voltar ao topo</a></p>

<!-- STACKS -->

[bs4-url]: https://beautiful-soup-4.readthedocs.io/en/latest/
[bs4-badge]: https://img.shields.io/badge/Beautiful_Soup-343131?style=for-the-badge&logo=8&logoColor=white
[flake8-url]: https://flake8.pycqa.org/en/latest/
[flake8-badge]: https://img.shields.io/badge/Flake8-000000?style=for-the-badge&logo=flake8&logoColor=white
[mongodb-url]: https://www.mongodb.com/
[mongodb-badge]: https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white
[pymongo-url]: https://pymongo.readthedocs.io/en/stable/
[pymongo-badge]: https://img.shields.io/badge/Pymongo-eeeeee?logo=pymongo&logoColor=white&style=for-the-badge
[pytest-url]: https://docs.pytest.org/en/7.2.x/
[pytest-badge]: https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white&style=for-the-badge
[python-url]: https://www.python.org/
[python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

<!-- CONTACT -->

[gmail-badge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[gmail-url]: mailto:garciaguig@gmail.com
[linkedin-badge]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/garciaagui/
[github-badge]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/garciaagui
[instagram-badge]: https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white
[instagram-url]: https://www.instagram.com/garciaagui/

<!-- OTHERS LINKS -->

[trybe-site-url]: https://www.betrybe.com/
[trybe-blog-url]: https://blog.betrybe.com/
