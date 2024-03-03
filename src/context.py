from typing import Dict

from promise.dataloader import DataLoader

from dataloaders import CountryLoader, NewsLoader

DATA_LOADER_COUNTRIES = "countries"
DATA_LOADER_NEWS = "news"

def register_dataloaders() -> Dict[str, DataLoader]:
    """
    Регистрация загрузчиков данных.

    :return:
    """

    return {DATA_LOADER_COUNTRIES: CountryLoader(), DATA_LOADER_NEWS: NewsLoader()}


def get_context() -> Dict[str, Dict[str, DataLoader]]:
    """
    Формирование контекста для представления схемы GraphQL.

    :return:
    """

    return {"dataloaders": register_dataloaders()}
