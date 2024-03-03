import pytest

from dataloaders import CountryLoader
from models.countries import CountryModel


class TestCountryLoader:
    @pytest.fixture
    def loader(self):
        return CountryLoader()

    def test_load_one_country(self, loader):
        country: CountryModel = loader.load("RU").get()
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

    def test_load_many_countries(self, loader):
        countries: list[CountryModel] = loader.load_many(["RU", "IE", "RS"]).get()
        assert len(countries) == 3
