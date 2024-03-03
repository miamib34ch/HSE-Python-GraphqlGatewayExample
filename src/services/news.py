import json
import os

from models.news import NewsModel


class NewsService:
    """
    Сервис для работы с данными о новостях.
    """

    @staticmethod
    def get_news() -> dict[str, list[NewsModel]]:
        """
        Получение списка новостей.

        :return:
        """
        news_dir = "fixtures/news/"
        base_dir = os.path.dirname(os.path.dirname(__file__))
        news_dir = os.path.join(base_dir, news_dir)
        files = os.listdir(news_dir)
        result = {}
        for news_file in files:
            alpha2code = news_file.split(".")[0]
            with open(news_dir + news_file, encoding="utf-8") as file:
                if data := json.load(file):
                    result[alpha2code] = [
                        NewsModel(
                            author=article.get("author"),
                            source=article.get("source").get("name"),
                            title=article.get("title"),
                            description=article.get("description"),
                            url=article.get("url"),
                            url_to_image=article.get("urlToImage"),
                            published_at=article.get("publishedAt"),
                            content=article.get("content"),
                        )
                        for article in data.get("articles", [])
                    ]
        return result