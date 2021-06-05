import requests

class CovidRepository:
    def getAllCountries():
        res = requests.get('https://api.covid19api.com/countries')
        if res.status_code != 200:
            print(res)
            raise Exception
        res.json()
        