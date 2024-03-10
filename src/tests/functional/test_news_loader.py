from datetime import datetime

import pytest

from dataloaders import NewsLoader
from models.news import NewsModel


class TestNewsLoader:
    @pytest.fixture
    def loader(self):
        return NewsLoader()

    def test_load_one_news(self, loader):
        news: list[NewsModel] = loader.load("RU").get()

        assert len(news) == 3
        news_item = news[0]
        assert news_item.author == "https://www.facebook.com/bbcnews"
        assert news_item.source == "BBC News"
        assert (
            news_item.title
            == "Vladimir Putin to give annual address to the nation in Moscow"
        )
        assert (
            news_item.description
            == "The major speech comes two years after the full-scale invasion of Ukraine - and a day before Alexei Navalny's funeral."
        )
        assert news_item.url == "https://www.bbc.co.uk/news/live/world-europe-68431017"

    def test_load_many_news(self, loader):
        news: list[list[NewsModel]] = loader.load_many(["RU", "IE", "RS"]).get()
        assert len(news) == 3
