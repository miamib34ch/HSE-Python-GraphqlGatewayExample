from datetime import date

import pytest

from schema import Query


class TestQuery:
    """
    Тесты для схемы Query
    """
    @pytest.fixture
    def query(self):
        """Фикстура для Query"""
        return Query()

    def test_query_resolve_places(self, query):
        """
        Тестирование метода resolve_places
        """
        places = query.resolve_places(None, None)
        assert len(places) == 6

    def test_query_resolve_news(self, query):
        """
        Тестирование метода resolve_news
        """
        place = query.resolve_place(None, None, 1)
        assert place.id == 1
        assert place.city == "Perm"
        assert place.country == "RU"
        assert place.latitude == 58.0081
        assert place.longitude == 56.249
        assert place.locality == "Sverdlovsky City District"
        assert place.description == "Супер место!"
        assert place.created_at.date() == date(2022, 10, 29)
        assert place.created_at.date() == date(2022, 10, 29)