from datetime import datetime

from pydantic import BaseModel, Field


class NewsModel(BaseModel):
    """
    Модель для описания новостей.
    """

    author: str | None = Field(title="Автор")
    source: str = Field(title="Источник")
    title: str = Field(title="Заголовок")
    description: str | None = Field(title="Описание")
    url: str = Field(title="Ссылка")
    url_to_image: str | None = Field(title="Ссылка на изображение")
    published_at: datetime = Field(title="Дата публикации")
    content: str | None = Field(title="Содержание")
