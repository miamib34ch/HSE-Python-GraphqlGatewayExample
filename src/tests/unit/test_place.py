from datetime import datetime

import pytest
from graphql import ResolveInfo

from context import get_context
from models.countries import CountryModel
from models.news import NewsModel
from models.places import PlaceModel
from schema import Place


class TestPlace:
    """
    Тесты для схемы Place
    """

    @pytest.fixture
    def place_graphene(self):
        """Фикстура для Place"""
        return Place()

    @pytest.fixture
    def place_model(self):
        """
        Фикстура для PlaceModel
        """
        return PlaceModel(
            id=1,
            city="Perm",
            country="RU",
            latitude=58.0081,
            longitude=56.249,
            locality="Sverdlovsky City District",
            description="Супер место!",
            created_at=datetime(2022, 10, 29, 12, 0, 0),
            updated_at=datetime(2022, 10, 29, 12, 0, 0),
        )

    @pytest.fixture
    def resolve(self):
        """
        Фикстура для ResolveInfo
        """
        return ResolveInfo(
            "test", [], None, None, None, None, None, None, {}, context=get_context()
        )

    def test_resolve_news(self, place_graphene, place_model, resolve):
        """
        Тестирование метода resolve_news
        """
        news: list[NewsModel] = place_graphene.resolve_news(place_model, resolve).get()
        assert len(news) == 3
        assert isinstance(news[0], NewsModel)

    def test_resolve_country(self, place_graphene, place_model, resolve):
        """
        Тестирование метода resolve_country
        """
        country: CountryModel = place_graphene.resolve_country(
            place_model, resolve
        ).get()
        assert isinstance(country, CountryModel)
