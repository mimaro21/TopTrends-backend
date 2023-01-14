import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from main.models import Country, TwitterTrend, TwitterCountryTrend
from utils.apis.twitter import load_country_trends
from utils.aux_functions import load_countries

from datetime import datetime, timedelta

class CountryType(DjangoObjectType):
    class Meta:
        model = Country

class TwitterTrendType(DjangoObjectType):
    class Meta:
        model = TwitterTrend

class Query(ObjectType):

    all_countries = graphene.List(CountryType)

    def resolve_all_countries(self, info, **kwargs):

        load_countries()

        return Country.objects.all()

    country_twitter_trends = graphene.List(TwitterTrendType, country=graphene.String(), trends_number=graphene.Int())

    def resolve_country_twitter_trends(self, info, **kwargs):

        load_countries()

        name = kwargs.get('country') 
        trends_number = kwargs.get('trends_number') if kwargs.get('trends_number') else 5

        filtered_country = Country.objects.filter(name=name)

        if filtered_country.exists() and Country.objects.get(name=name).woeid != None:

            if TwitterCountryTrend.objects.filter(country__name=name).exists():
            
                twitter_country_trends = TwitterCountryTrend.objects.get(country__name=name)

                d1 = twitter_country_trends.insertion_datetime + timedelta(hours=1)
                d1 = datetime.strptime(str(d1).split("+")[0], "%Y-%m-%d %H:%M:%S.%f")
                
                d2 = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")

                if d1 < d2 - timedelta(hours=1) or twitter_country_trends.trends_number != trends_number:
                    load_country_trends(name, trends_number)

            else:
                load_country_trends(name, trends_number)

            return TwitterTrend.objects.filter(country_trend__country__name=name)                

        return []

schema = graphene.Schema(query=Query)