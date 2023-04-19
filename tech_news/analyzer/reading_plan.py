from typing import Any, Dict, List
from tech_news.database import find_news


class ReadingPlanService:
    @staticmethod
    def _db_news_proxy():
        """
        This proxy exists so that it is possible to mock
        the `find_news` function of the `tech_news.database`.
        """
        return find_news()

    @classmethod
    def group_news_for_available_time(
        cls, available_time: int
    ) -> Dict[str, List]:
        if available_time <= 0:
            raise ValueError("'available_time' must be greater than zero")

        result = {"readable": [], "unreadable": []}
        for new in cls._db_news_proxy():
            if new["reading_time"] > available_time:
                cls._register_unreadable(result, new)
                continue

            if cls._fit_to_existing_group(result, new):
                continue

            cls._register_readable(available_time, result, new)
        return result

    @classmethod
    def _register_readable(
        cls, available_time: int, result: Dict[str, List], new: Dict[str, Any]
    ):
        result["readable"].append(
            {
                "unfilled_time": available_time - new["reading_time"],
                "chosen_news": [(new["title"], new["reading_time"])],
            }
        )

    @classmethod
    def _register_unreadable(
        cls, result: Dict[str, List], new: Dict[str, Any]
    ):
        result["unreadable"].append((new["title"], new["reading_time"]))

    @classmethod
    def _fit_to_existing_group(
        cls, result: Dict[str, List], new: Dict[str, Any]
    ):
        for group in result["readable"]:
            if new["reading_time"] >= group["unfilled_time"]:
                continue

            group["unfilled_time"] -= new["reading_time"]
            group["chosen_news"].append((new["title"], new["reading_time"]))
            return True

        return False
