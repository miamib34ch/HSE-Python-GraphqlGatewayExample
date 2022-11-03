from typing import Optional

import graphene
from graphene import Schema
from graphql import ResolveInfo
from promise import Promise

from context import DATA_LOADER_COUNTRIES
from models.places import PlaceModel
from services.places import PlacesService


class Country(graphene.ObjectType):
    """
    Тип объекта страны.
    """

    name = graphene.String()
    alpha2code = graphene.String()
    alpha3code = graphene.String()
    capital = graphene.String()
    region = graphene.String()
    subregion = graphene.String()
    population = graphene.Int()
    latitude = graphene.Float()
    longitude = graphene.Float()
    demonym = graphene.String()
    area = graphene.Float()
    numeric_code = graphene.Int()
    flag = graphene.String()
    currencies = graphene.List(graphene.String)
    languages = graphene.List(graphene.String)


class Place(graphene.ObjectType):
    """
    Тип объекта любимого места.
    """

    latitude = graphene.Float()
    longitude = graphene.Float()
    description = graphene.String()
    city = graphene.String()
    locality = graphene.String()
    country = graphene.Field(Country)

    @staticmethod
    def resolve_country(parent: PlaceModel, info: ResolveInfo) -> Promise:
        """
        Получение связанной информации о странах для объектов любимых мест.

        :param parent: Объект любимого места.
        :param info: Объект с метаинформацией и данных о контексте запроса.
        :return:
        """

        if info.context:
            dataloaders = info.context["dataloaders"]

            return dataloaders[DATA_LOADER_COUNTRIES].load(str(parent.country))

        return Promise.resolve([])


class Query(graphene.ObjectType):
    """
    Общий тип для запроса получения данных.
    """

    places = graphene.List(Place)

    @staticmethod
    def resolve_places(
        parent: Optional[dict], info: ResolveInfo  # pylint: disable=unused-argument
    ) -> list[PlaceModel]:
        return PlacesService().get_places()


schema = Schema(query=Query)
