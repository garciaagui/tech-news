from unittest.mock import Mock, patch
from tech_news.analyzer.reading_plan import ReadingPlanService
import pytest


@pytest.fixture
def mocked_find_news_data():
    mock = Mock()
    mock.return_value = [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia bacana",
            "timestamp": "04/04/2021",
            "writer": "J. R. R. Tolkien",
            "reading_time": 4,
            "summary": "Algo bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-muito-bacana",
            "title": "Notícia muito bacana",
            "timestamp": "07/09/2022",
            "writer": "Alan Moore",
            "reading_time": 10,
            "summary": "Algo muito bacana aconteceu",
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacaníssima",
            "title": "Notícia bacaníssima",
            "timestamp": "02/03/2023",
            "writer": "Frank Miller",
            "reading_time": 15,
            "summary": "Algo bacaníssima aconteceu",
            "category": "Carreira",
        },
    ]
    return mock


def test_reading_plan_group_news(mocked_find_news_data):

    expected = {
        "readable": [
            {
                "unfilled_time": 6,
                "chosen_news": [("Notícia bacana", 4)],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [("Notícia muito bacana", 10)],
            },
        ],
        "unreadable": [("Notícia bacaníssima", 15)],
    }

    with patch.object(
        ReadingPlanService, "_db_news_proxy", mocked_find_news_data
    ):

        # Valid input
        result = ReadingPlanService.group_news_for_available_time(10)
        assert result == expected

        # Invalid input
        with pytest.raises(
            ValueError,
            match="Valor 'available_time' deve ser maior que zero",
        ):
            ReadingPlanService.group_news_for_available_time(-1)
