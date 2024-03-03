from datetime import date, datetime

from services.countries import CountriesService
from services.places import PlacesService
from services.news import NewsService


def test_read_news():
    """
    Тестирование сервиса новостей
    """
    news = NewsService.get_news()
    assert len(news) == 3
    assert news.keys() == {"ru", "ie", "rs"}
    ru_news = news["ru"]
    assert len(ru_news) == 3
    news_item = ru_news[0]
    assert news_item.author == "https://www.facebook.com/bbcnews"
    assert news_item.source == "BBC News"


def test_read_places():
    """
    Тестирование сервиса мест
    """
    places = PlacesService().get_places()
    assert len(places) == 6

    place = places[0]
    assert place.id == 1
    assert place.city == "Perm"
    assert place.country == "RU"
    assert place.latitude == 58.0081
    assert place.longitude == 56.249
    assert place.locality == "Sverdlovsky City District"
    assert place.description == "Супер место!"
    assert place.created_at.date() == date(2022, 10, 29)
    assert place.created_at.date() == date(2022, 10, 29)


def test_read_place():
    """
    Тестирование сервиса мест
    """
    place = PlacesService().get_place(1)
    assert place.id == 1
    assert place.city == "Perm"
    assert place.country == "RU"
    assert place.latitude == 58.0081
    assert place.longitude == 56.249
    assert place.locality == "Sverdlovsky City District"
    assert place.description == "Супер место!"
    assert place.created_at.date() == date(2022, 10, 29)
    assert place.created_at.date() == date(2022, 10, 29)


def test_read_countries():
    """
    Тестирование сервиса стран
    """
    countries = CountriesService().get_countries()
    assert len(countries) == 4

    country = countries[1]
    assert country.name == "Russian Federation"
    assert country.alpha2code == "RU"
    assert country.alpha3code == "RUS"
    assert country.capital == "Moscow"
    assert country.region == "Europe"
    assert country.subregion == "Eastern Europe"
    assert country.population == 146599183
    assert country.latitude == 60.0
    assert country.longitude == 100.0
    assert country.demonym == "Russian"
    assert country.area == 17124442.0
    assert country.numeric_code == "643"
    assert country.flag == "http://assets.promptapi.com/flags/RU.svg"
    assert country.currencies == ["RUB"]
    assert country.languages == ["Russian"]