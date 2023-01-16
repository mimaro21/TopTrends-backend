import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from main.models import Country, TwitterTrend, TwitterCountryTrend, GoogleTrend, GoogleCountryTrend

from utils.apis.twitter import load_country_trends as load_twitter_country_trends
from utils.apis.google_trends import load_country_trends as load_google_country_trends
from utils.aux_functions import setup_countries, remove_cache

class CountryType(DjangoObjectType):
    class Meta:
        model = Country

class TwitterTrendType(DjangoObjectType):
    class Meta:
        model = TwitterTrend

class GoogleTrendType(DjangoObjectType):
    class Meta:
        model = GoogleTrend

class Query(ObjectType):

    all_countries = graphene.List(CountryType)

    def resolve_all_countries(self, info, **kwargs):

        load_countries()

        return Country.objects.all()

    country_twitter_trends = graphene.List(TwitterTrendType, country=graphene.String(), trends_number=graphene.Int())

    def resolve_country_twitter_trends(self, info, **kwargs):

        name, trends_number, filtered_country = setup_countries(kwargs)

        if filtered_country.exists() and Country.objects.get(name=name).woeid != None:

            if TwitterCountryTrend.objects.filter(country__name=name).exists():
            
                twitter_country_trends = TwitterCountryTrend.objects.get(country__name=name)

                cond_1 = remove_cache(twitter_country_trends)

                if cond_1:
                    load_twitter_country_trends(name)

            else:
                load_twitter_country_trends(name)

            return TwitterTrend.objects.filter(country_trend__country__name=name)[:trends_number]      

        return []

    country_google_trends = graphene.List(GoogleTrendType, country=graphene.String(), trends_number=graphene.Int())

    def resolve_country_google_trends(self, info, **kwargs):

        name, trends_number, filtered_country = setup_countries(kwargs)

        if filtered_country.exists() and Country.objects.get(name=name).pn != None:

            if GoogleCountryTrend.objects.filter(country__name=name).exists():
            
                google_country_trends = GoogleCountryTrend.objects.get(country__name=name)

                cond_1 = remove_cache(google_country_trends)

                if cond_1:
                    load_google_country_trends(name)

            else:
                load_google_country_trends(name)

            return GoogleTrend.objects.filter(country_trend__country__name=name)[:trends_number]         

        return []

schema = graphene.Schema(query=Query)