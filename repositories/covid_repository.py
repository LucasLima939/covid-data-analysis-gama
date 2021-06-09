import requests
import json
from service.s3_service import S3Service
from datetime import datetime
from datetime import timedelta

class CovidRepository:
    def get_all_countries(self):
        res = requests.get('https://api.covid19api.com/countries')
        if res.status_code != 200:
            print(res)
            raise Exception
        countries_json = res.json()
        return list(map(lambda x: x['Slug'], countries_json))

    def get_all_countries_covid_infos(self, countriesSlugs):
        s3_service = S3Service()
        self.countries_json_list = list()
        self.cases_json_list = list()  

        for slug in countriesSlugs:
            if slug == 'united-states':
                CovidRepository.getUnitedStatesInfos()
            else:
                covid_info_list = CovidRepository.get_country_covid_infos(slug, slug, None, None)
                if not covid_info_list:
                    print('empty list')
                else:
                    CovidRepository.extract_country_from_json(covid_info_list[0])

                    CovidRepository.extract_case_from_json_list(covid_info_list)
            
        s3_service.upload_list_json(self.countries_json_list, 'countries_json')
        s3_service.upload_list_json(self.cases_json_list, 'covid_infos_json')

    def extract_country_from_json(self, info):
        country = {}
        country['Country'] = info['Country']
        country['CountryCode'] = info['CountryCode']
        country['Lat'] = info['Lat']
        country['Lon'] = info['Lon']
        json_country = json.dumps(country)
        self.countries_json_list.append(json_country)

    
    def extract_case_from_json_list(self, covid_info_list):
        for info in covid_info_list:
            case = {}
            case['Confirmed'] = info['Confirmed']
            case['Deaths'] = info['Deaths']
            case['Recovered'] = info['Recovered']
            case['Active'] = info['Active']
            case['Date'] = info['Date']
            case['CountryCode'] = info['CountryCode']
            json_case = json.dumps(case)
            self.cases_json_list.append(json_case)

                
    def getUnitedStatesInfos(self):
        current_date = datetime(2020,1,1)
        final_date = datetime(2021,6,7)
        while current_date <= final_date:
            current_date += timedelta(days=7)
            to_date = current_date + timedelta(days=7)
            covid_info_list = CovidRepository.get_country_covid_infos('united-states', current_date.strftime("%Y-%m-%dT%H:%M:%SZ"), to_date.strftime("%Y-%m-%dT%H:%M:%SZ"))
            if(current_date <= final_date):
                CovidRepository.extract_country_from_json(covid_info_list[0])
            CovidRepository.extract_case_from_json_list(covid_info_list)



    def get_country_covid_infos(self, slug, from_date, to_date):
        if from_date is None:
            from_date = '2020-01-01T00:00:00Z'
        if to_date is None:
            to_date = '2021-06-07T00:00:00Z'
        url = 'https://api.covid19api.com/country/%s?from=%s&to=%s' % (slug, from_date, to_date)

        res = requests.get(url)

        if res.status_code != 200:
            print(res)
            return []

        return res.json()


        