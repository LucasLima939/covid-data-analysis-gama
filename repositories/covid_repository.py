import requests
import json

class CovidRepository:
    def getAllCountries(self):
        res = requests.get('https://api.covid19api.com/countries')
        if res.status_code != 200:
            print(res)
            raise Exception
        countriesJson = res.json()
        countryList = list()
        for country in countriesJson:
            countryList.append(country['Slug'])
        return countryList

    def getAllCountriesCovidInfos(self, countriesSlugs):
        countriesJsonList = list()
        casesJsonList = list()  

        for slug in countriesSlugs:
            covidInfoList = CovidRepository.getCountryCovidInfos(slug, slug, None, None)
            if not covidInfoList:
                print('empty list')
            else:
                country = {}
                country['Country'] = covidInfoList[0]['Country']
                country['CountryCode'] = covidInfoList[0]['CountryCode']
                country['Lat'] = covidInfoList[0]['Lat']
                country['Lon'] = covidInfoList[0]['Lon']
                json_country = json.dumps(country)
                countriesJsonList.append(json_country)

                for info in covidInfoList:
                    case = {}
                    case['Confirmed'] = info['Confirmed']
                    case['Deaths'] = info['Deaths']
                    case['Recovered'] = info['Recovered']
                    case['Active'] = info['Active']
                    case['Date'] = info['Date']
                    case['CountryCode'] = info['CountryCode']
                    json_case = json.dumps(case)
                    casesJsonList.append(json_case)

                

    def getCountryCovidInfos(self, slug, fromDate, toDate):
        if fromDate is None:
            fromDate = '2020-01-01T00:00:00Z'
        if toDate is None:
            toDate = '2021-06-07T00:00:00Z'
        url = 'https://api.covid19api.com/country/%s?from=%s&to=%s' % (slug, fromDate, toDate)

        res = requests.get(url)

        if res.status_code != 200:
            print(res)
            raise Exception

        return res.json()


        