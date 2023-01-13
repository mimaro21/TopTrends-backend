import tweepy
from decouple import config
from main.models import Country

def api_setup():
    
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(config('TWITTER_API_KEY'), config('TWITTER_SECRET_API_KEY'))
    auth.set_access_token(config('TWITTER_ACCESS_TOKEN'), config('TWITTER_SECRET_ACCESS_TOKEN'))

    # Create API object
    api = tweepy.API(auth)
    return api

def trend_countries():
    
    api = api_setup()
    
    # Get countries that have trends
    trends_available = api.available_trends()

    countries = {}
    acronyms = {}
    for i in range(len(trends_available)):
        if trends_available[i]['country'] not in countries:
            if trends_available[i]['country'] != '':
                countries[trends_available[i]['country']] = trends_available[i]['woeid']
                acronyms[trends_available[i]['country']] = trends_available[i]['countryCode']
            else:
                countries[trends_available[i]['name']] = trends_available[i]['woeid']
                acronyms[trends_available[i]['name']] = 'WW'

    return (countries, acronyms)

def load_twitter_countries():

    n_countries = Country.objects.count()

    if n_countries == 0:

        countries, acronyms = trend_countries()

        for country in countries:
            c = Country(name=country, acronym=acronyms[country], woeid=countries[country])
            c.save()