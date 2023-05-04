<a name="readme-top"></a>

<h1 align="center">Tech News 📰</h1>

> [🇧🇷 Clique aqui para acessar a versão em português.](README_pt-br.md)

## Summary

<ol>
  <li><a href="#description">Description</a></li>
  <li><a href="#technologies">Technologies</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#how-to-run">How to Run</a></li>
  <li><a href="#about-trybe">About Trybe</a></li>
  <li><a href="#contact">Contact</a></li>
</ol>

## Description

**31st project** of the [Trybe][trybe-site-url] Web Development course.

Tech News is a [Python][python-url] project that uses [Beautiful Soup][bs4-url] to perform web scraping on [Trybe's blog][trybe-blog-url] and fetch tech news and articles, storing them in a [MongoDB][mongodb-url] database.

> ℹ️ I wrote tests for the functions implemented by Trybe. These tests can be found in the `tests` subdirectory.

<br/>

## Technologies

The project was developed in [Python][python-url] and tested with [Pytest][pytest-url]. The database used was [MongoDB][mongodb-url] and the connection and interaction to it was established through the [PyMongo][pymongo-url] library. [Flake8][flake8-url] ensured code quality while [Beautiful Soup][bs4-url] performed web scraping.

[![Python][python-badge]][python-url] [![MongoDB][mongodb-badge]][mongodb-url] [![PyMongo][pymongo-badge]][pymongo-url] [![Beautiful Soup][bs4-badge]][bs4-url] [![Pytest][pytest-badge]][pytest-url] [![Flake8][flake8-badge]][flake8-url]

<br/>

## Features

<ul>
  <li>Collect news and articles from Trybe's blog using web scraping and store them in a MongoDB database.</li>
  <li>Search news by title.</li>
  <li>Search news by date.</li>
  <li>Browse news by category.</li>
  <li>List the top 5 categories with the most news.</li>
</ul>

<br/>

## How to Run

To run the project locally, follow the steps below.

1. Clone the repository.

```
git clone git@github.com:garciaagui/tech-news.git
```

2. Navigate to the root of the project.

```
cd tech-news/
```

3. Create the virtual environment.

```
python3 -m venv .venv
```

4. Activate the virtual environment.

```
source .venv/bin/activate
```

-   Note that at the beginning of the terminal line there will be `(.venv)`, as in the example below.

```
(.venv) gui@gui-desktop:~/Trybe/tech-news$
```

-   To deactivate the virtual environment, run the command `deactivate`. Remember to activate it again when you return to the project.

5. Install dependencies in the virtual environment.

```
python3 -m pip install -r dev-requirements.txt
```

6. If you don't have MongoDB installed locally, launch it via Docker.

```
docker-compose up -d mongodb
```

-   ℹ️ Database name is `tech_news`.

7. Run the following command to access the menu.

```
tech-news-analyzer
```

<details>
  <summary><strong> ℹ️ For additional instructions, click here.</strong></summary><br />

-   🧪 To run **all** tests, execute the command below.

```
python3 -m pytest
```

-   🧪 To run only one test file, follow the example below.

```
python3 -m pytest tests/reading_plan/test_reading_plan.py
```

-   🧪 To run only one specific test, follow the example below.

```
python3 -m pytest -k test_reading_plan_group_news_with_valid_input
```

-   If you wish to manually test directly in the modules where the functions were implemented, follow the example below.

```
python3 -m tech_news.scraper.py
```

</details>

<br/>

## About Trybe

_"[Trybe][trybe-site-url] is a future school for anyone who wants to improve their lives and build a successful career in technology, where the person only pays when they get a good job."_

_"The program features over 1,500 hours of online classes covering introduction to software development, front-end, back-end, computer science, software engineering, agile methodologies, and behavioral skills."_

<br/>

## Contact

Project developed by **Guilherme Garcia**. Below are my social networks and means of contact. 🤘

[![Gmail][gmail-badge]][gmail-url]
[![Linkedin][linkedin-badge]][linkedin-url]
[![GitHub][github-badge]][github-url]
[![Instagram][instagram-badge]][instagram-url]

<p align="right"><a href="#readme-top">Back to top</a></p>

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
