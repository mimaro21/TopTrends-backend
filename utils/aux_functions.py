from utils.apis.twitter import trend_countries
from utils.apis.google_trends import google_trends_countries

from main.models import Country

from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

### Auxiliar functions to use in schema.py ###

def load_countries():

    n_countries = Country.objects.count()

    if n_countries == 0:

        # Load countries from Twitter trends
        twitter_countries, twitter_acronyms = trend_countries()

        # Load countries from Google Trends
        gt_countries = google_trends_countries()

        all_countries = set([country for country in twitter_countries] + [country for country in gt_countries])
        all_countries = list(all_countries)

        for country in all_countries:

            acronym, woeid, country_pn = None, None, None

            if country in twitter_countries:
                acronym = twitter_acronyms[country]
                woeid = twitter_countries[country]
            if country in gt_countries:
                country_pn = gt_countries[country]
                
            c = Country(name=country, acronym=acronym, woeid=woeid, pn=country_pn)
            c.save()

def setup_countries(kwargs):

    load_countries()

    name = kwargs.get('country') 
    trends_number = kwargs.get('trends_number') if kwargs.get('trends_number') else 5

    filtered_country = Country.objects.filter(name=name)

    return name, trends_number, filtered_country

def remove_cache(obj):

    d1 = obj.insertion_datetime + timedelta(hours=1)
    d1 = datetime.strptime(str(d1).split("+")[0], DATE_FORMAT)
    
    d2 = datetime.strptime(str(datetime.now()), DATE_FORMAT)

    if d1 < d2 - timedelta(hours=1):
        return True
    return False