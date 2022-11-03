from typing import Dict

from promise.dataloader import DataLoader

from dataloaders import CountryLoader

DATA_LOADER_COUNTRIES = "countries"


def register_dataloaders() -> Dict[str, DataLoader]:
    """
    Регистрация загрузчиков данных.

    :return:
    """

    return {DATA_LOADER_COUNTRIES: CountryLoader()}


def get_context() -> Dict[str, Dict[str, DataLoader]]:
    """
    Формирование контекста для представления схемы GraphQL.

    :return:
    """

    return {"dataloaders": register_dataloaders()}
