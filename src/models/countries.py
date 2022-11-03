from pydantic import BaseModel, Field


class CountryModel(BaseModel):
    """
    Модель для описания страны.
    """

    name: str = Field(title="Название страны")
    alpha2code: str = Field(title="ISO Alpha2")
    alpha3code: str = Field(title="ISO Alpha3")
    capital: str = Field(title="Столица")
    region: str = Field(title="Регион")
    subregion: str = Field(title="Субрегион")
    population: int = Field(title="Население")
    latitude: float = Field(title="Широта")
    longitude: float = Field(title="Долгота")
    demonym: str = Field(title="Название жителей")
    area: float = Field(title="Площадь")
    numeric_code: str = Field(title="Трёхзначный код страны")
    flag: str = Field(title="Флаг")
    currencies: list[str] = Field(title="Валюты")
    languages: list[str] = Field(title="Языки")
