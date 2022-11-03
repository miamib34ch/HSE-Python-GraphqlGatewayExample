import json

from models.countries import CountryModel


class CountriesService:
    """
    Сервис для работы с данными о странах.
    """

    def get_countries(self) -> list[CountryModel]:
        """
        Получение списка стран.

        :return:
        """

        result = []
        with open("fixtures/countries.json", encoding="utf-8") as file:
            if data := json.load(file):
                result = [
                    CountryModel(
                        name=country.get("name"),
                        alpha2code=country.get("alpha2code"),
                        alpha3code=country.get("alpha3code"),
                        capital=country.get("capital"),
                        region=country.get("region"),
                        subregion=country.get("subregion"),
                        population=country.get("population"),
                        latitude=country.get("latitude"),
                        longitude=country.get("longitude"),
                        demonym=country.get("demonym"),
                        area=country.get("area"),
                        numeric_code=country.get("numeric_code"),
                        flag=country.get("flag"),
                        currencies=country.get("currencies"),
                        languages=country.get("languages"),
                    )
                    for country in data
                ]

        return result
