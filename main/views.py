from utils.apis.twitter import get_country_trends

def aa(request):
    print(get_country_trends(country='Argentina'))