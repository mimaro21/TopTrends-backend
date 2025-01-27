import tweepy
from decouple import config
import json
from main.models import Country, TwitterTrend, TwitterCountryTrend
import re
from googletrans import Translator
import emoji

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

def get_country_trends(country_name):

    try:
        country = Country.objects.get(name=country_name)
        woeid = country.woeid

        api = api_setup()

        country_trends = api.get_place_trends(woeid)
        country_trends_json = json.dumps(country_trends)
        country_trends_dict = json.loads(country_trends_json)
        country_trends_list = country_trends_dict[0]['trends'][:25]

        res = []
        for t in country_trends_list:
            res.append((t['name'], t['url'], t['tweet_volume']))

        return res
    except:
        return []

def load_country_trends(country_name):

    trends = get_country_trends(country_name)

    if len(trends) > 0:

        country = Country.objects.get(name=country_name)

        if TwitterCountryTrend.objects.filter(country=country).exists():
            TwitterCountryTrend.objects.filter(country=country).delete()

        tct = TwitterCountryTrend(country=country)
        tct.save()

        for t in trends:
            t = TwitterTrend.objects.create(name=t[0], url=t[1], tweet_volume=t[2], country_trend=tct)
            t.save()

def translate_to_english(text):
    translator = Translator()
    text_en = translator.translate(text, dest='en').text

    return text_en

def get_relevant_tweets(trend):

    api = api_setup()

    tweets = api.search_tweets(q=trend, count=20, result_type='popular')

    res = []

    for tweet in tweets:
        if not tweet.retweeted and 'RT @' not in tweet.text:
            tweet = translate_to_english(tweet.text)            
            no_emoji_text = emoji.get_emoji_regexp().sub(u'', tweet)
            no_url_text = re.sub(r"http\S+", "", no_emoji_text)
            no_mention_text = re.sub(r"@\S+", "", no_url_text)
            no_hashtag_text = re.sub(r"#\S+", "", no_mention_text)
            clean_tweet = no_hashtag_text.replace('\n', ' ').replace('\r', '').strip()
            if clean_tweet != '':
                res.append(clean_tweet)

    return res