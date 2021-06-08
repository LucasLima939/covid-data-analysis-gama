import requests
import json
from service.s3_service import S3Service

class CovidRepository:
    def get_all_countries(self):
        res = requests.get('https://api.covid19api.com/countries')
        if res.status_code != 200:
            print(res)
            raise Exception
        countries_json = res.json()
        country_list = list()
        for country in countries_json:
            country_list.append(country['Slug'])
        return country_list

    def get_all_countries_covid_infos(self, countriesSlugs):
        s3_service = S3Service()
        countries_json_list = list()
        cases_json_list = list()  

        for slug in countriesSlugs:
            covid_info_list = CovidRepository.get_country_covid_infos(slug, slug, None, None)
            if not covid_info_list:
                print('empty list')
            else:
                country = {}
                country['Country'] = covid_info_list[0]['Country']
                country['CountryCode'] = covid_info_list[0]['CountryCode']
                country['Lat'] = covid_info_list[0]['Lat']
                country['Lon'] = covid_info_list[0]['Lon']
                json_country = json.dumps(country)
                countries_json_list.append(json_country)

                for info in covid_info_list:
                    case = {}
                    case['Confirmed'] = info['Confirmed']
                    case['Deaths'] = info['Deaths']
                    case['Recovered'] = info['Recovered']
                    case['Active'] = info['Active']
                    case['Date'] = info['Date']
                    case['CountryCode'] = info['CountryCode']
                    json_case = json.dumps(case)
                    cases_json_list.append(json_case)

        s3_service.upload_list_json(countries_json_list)
        s3_service.upload_list_json(cases_json_list)

                

    def get_country_covid_infos(self, slug, from_date, to_date):
        if from_date is None:
            from_date = '2020-01-01T00:00:00Z'
        if to_date is None:
            to_date = '2021-06-07T00:00:00Z'
        url = 'https://api.covid19api.com/country/%s?from=%s&to=%s' % (slug, from_date, to_date)

        res = requests.get(url)

        if res.status_code != 200:
            print(res)
            raise Exception

        return res.json()


        