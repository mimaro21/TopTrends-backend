import requests

def all_countries():

    url = "https://restcountries.com/v2/all"

    response = requests.get(url)
    countries = []

    if response.status_code == 200:
        
        data = response.json()

        for country in data:
            name = parse_country_name(country['name'])
            native_name = country['nativeName']
            alpha2_code = country['alpha2Code']
            flag = country['flag']
            aux = (name, native_name, alpha2_code, flag)
            countries.append(aux)

    return countries