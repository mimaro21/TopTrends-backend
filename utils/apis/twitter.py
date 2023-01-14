import tweepy
from decouple import config
import json
from main.models import Country, TwitterTrend, TwitterCountryTrend

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

# Get trends of a country

def get_country_trends(country_name, n_trends=10):

    try:
        country = Country.objects.get(name=country_name)
        woeid = country.woeid

        api = api_setup()

        country_trends = api.get_place_trends(woeid)
        country_trends_json = json.dumps(country_trends)
        country_trends_dict = json.loads(country_trends_json)
        country_trends_list = country_trends_dict[0]['trends'][:n_trends]

        res = []
        for t in country_trends_list:
            res.append((t['name'], t['url'], t['tweet_volume']))

        return res
    except:
        return []

def load_country_trends(country_name, n_trends=10):

    trends = get_country_trends(country_name, n_trends)

    if len(trends) > 0:

        country = Country.objects.get(name=country_name)

        if TwitterCountryTrend.objects.filter(country=country).exists():
            TwitterCountryTrend.objects.filter(country=country).delete()

        tct = TwitterCountryTrend(country=country, trends_number=n_trends)
        tct.save()

        for t in trends:
            t = TwitterTrend.objects.create(name=t[0], url=t[1], tweet_volume=t[2], country_trend=tct)
            t.save()
