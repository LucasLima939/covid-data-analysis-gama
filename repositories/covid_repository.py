import requests

class CovidRepository:
    def getAllCountries(self):
        res = requests.get('https://api.covid19api.com/countries')
        if res.status_code != 200:
            print(res)
            raise Exception
        countriesJson = res.json()
        countryList = list()
        for country in countriesJson:
            countryList.append(country['Country'])
        print(countryList)
        