import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from utils.apis.twitter import load_twitter_countries

from main.models import Country

class CountryType(DjangoObjectType):
    class Meta:
        model = Country

class Query(ObjectType):
    countries = graphene.List(CountryType)

    def resolve_countries(self, info, **kwargs):

        load_twitter_countries()

        return Country.objects.all()

schema = graphene.Schema(query=Query)