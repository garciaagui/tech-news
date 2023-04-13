import requests
import time


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


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
