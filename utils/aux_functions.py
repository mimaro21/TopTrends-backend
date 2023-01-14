from utils.apis.twitter import trend_countries
from utils.apis.google_trends import google_trends_countries

from main.models import Country

def load_countries():

    n_countries = Country.objects.count()

    if n_countries == 0:

        # Load countries from Twitter trends
        twitter_countries, twitter_acronyms = trend_countries()

        # Load countries from Google Trends
        gt_countries = google_trends_countries()

        all_countries = set([country for country in twitter_countries] + [country for country in gt_countries])
        all_countries = list(all_countries)

        print("ss")

        for country in all_countries:

            acronym, woeid, country_pn = None, None, None

            if country in twitter_countries:
                acronym = twitter_acronyms[country]
                woeid = twitter_countries[country]
            if country in gt_countries:
                country_pn = gt_countries[country]
                
            c = Country(name=country, acronym=acronym, woeid=woeid, pn=country_pn)
            c.save()