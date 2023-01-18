import re
from pytrends.request import TrendReq

from main.models import Country, GoogleTrend, GoogleCountryTrend

# Convert snake_case to Title Case

def snake_to_title(string):
    words = re.findall(r'[a-zA-Z0-9]+', string)
    title_case = ' '.join([word.capitalize() for word in words])
    return title_case

pytrends = TrendReq(hl='en-US', tz=360)

def google_trends_countries():

    req_json = pytrends._get_data(
        url='https://trends.google.com/trends/hottrends/visualize/internal/data',
        method='get'
    )

    countries = {}

    for country in req_json:
        countries[snake_to_title(country)] = country

    return countries

def get_country_trends(country_name):

    try:

        country = Country.objects.get(name=country_name)
        pn = country.pn

        country_trends = pytrends.trending_searches(pn=pn)
        country_trends_list = country_trends.values.tolist()

        res = []
        for t in country_trends_list:
            res.append(t[0])

        return res
    except:
        return []

def load_country_trends(country_name):

    trends = get_country_trends(country_name)

    if len(trends) > 0:

        country = Country.objects.get(name=country_name)

        if GoogleCountryTrend.objects.filter(country=country).exists():
            GoogleCountryTrend.objects.filter(country=country).delete()

        gct = GoogleCountryTrend(country=country)
        gct.save()

        for t in trends:
            t = GoogleTrend(name=t, country_trend=gct)
            t.save()