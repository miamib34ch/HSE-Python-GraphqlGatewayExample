from promise import Promise
from promise.dataloader import DataLoader

from services.countries import CountriesService
from services.news import NewsService


class CountryLoader(DataLoader):
    """
    Загрузчик данных о странах.
    """

    def batch_load_fn(  # pylint: disable=method-hidden
        self, alpha2codes: list[str]
    ) -> Promise:
        """
        Функция для загрузки связанных данных по переданному множеству значений.

        :param alpha2codes: Список ISO Alpha2-кодов стран
        :return:
        """

        countries = CountriesService().get_countries()
        countries_map = {country.alpha2code: country for country in countries}

        # формирование результата с сохранением порядка из alpha2codes
        return Promise.resolve([countries_map.get(code) for code in alpha2codes])


class NewsLoader(DataLoader):
    """
    Загрузчик данных о новостях.
    """

    def batch_load_fn(  # pylint: disable=method-hidden
        self, alpha2codes: list[str]
    ) -> Promise:
        """
        Функция для загрузки связанных данных по переданному множеству значений.

        :param alpha2codes: Список ISO Alpha2-кодов стран
        :return:
        """
        news = NewsService().get_news()

        return Promise.resolve([news.get(code.lower()) for code in alpha2codes if code])
