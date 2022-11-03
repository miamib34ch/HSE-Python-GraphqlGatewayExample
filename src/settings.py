from pydantic import BaseModel, BaseSettings, Field


class Project(BaseModel):
    """
    Описание проекта.
    """

    #: название проекта
    title: str = "GraphQL API Gateway"
    #: описание проекта
    description: str = "Шлюз для взаимодействия с микросервисами."
    #: версия релиза
    release_version: str = Field(default="0.1.0")


class Settings(BaseSettings):
    """
    Настройки проекта.
    """

    #: режим отладки
    debug: bool = Field(default=False)
    #: описание проекта
    project: Project = Project()
    #: базовый адрес приложения
    base_url: str = Field(default="http://0.0.0.0:8000")

    class Config:
        env_file = ".env"


# инициализация настроек приложения
settings = Settings()
