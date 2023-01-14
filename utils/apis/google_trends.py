import re
from pytrends.request import TrendReq

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