import requests
import json
from service.s3_service import S3Service
from datetime import datetime
from datetime import timedelta

class CovidRepository:
    def get_all_countries(self):
        print('getting all countries')
        res = requests.get('https://api.covid19api.com/countries')
        if res.status_code != 200:
            print(res)
            raise Exception
        countries_json = res.json()
        print('all countries retrieved successfully!')
        return list(map(lambda x: x['Slug'], countries_json))

    def get_all_countries_covid_infos(self, countriesSlugs):
        s3_service = S3Service()
        self.countries_json_list = list()
        self.cases_json_list = list()  
        print('INIT getting data for each country')
        print('-------------------------------')
        for slug in countriesSlugs:
            if slug == 'united-states':
                print('getting data from united-states')
                CovidRepository.getUnitedStatesInfos(self)
            else:
                covid_info_list = CovidRepository.get_country_covid_infos(slug, None, None)
                if not covid_info_list:
                    print('empty list from ' + slug)
                    print('-------------------------------')
                else:
                    CovidRepository.extract_country_from_json(self, covid_info_list[0])

                    CovidRepository.extract_case_from_json_list(self, covid_info_list)


                    print('all data from ' + slug + ' fetched')
                    print('COUNTRIES list lenght: ' +   str(len(self.countries_json_list)))
                    print('CASES list count: ' + str(len(self.cases_json_list)))
                    print('-------------------------------')
            
        print('all data recovered, initing upload to s3')
        s3_service.upload_list_json(self.countries_json_list, 'countries_json')
        s3_service.upload_list_json(self.cases_json_list, 'covid_infos_json')
        print('finished upload to s3')

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
            next_week = current_date + timedelta(days=7)
            from_date = current_date.strftime("%Y-%m-%dT%H:%M:%SZ")
            to_date = next_week.strftime("%Y-%m-%dT%H:%M:%SZ")
            covid_info_list = CovidRepository.get_country_covid_infos('united-states', from_date, to_date)
            if(current_date == final_date):
                CovidRepository.extract_country_from_json(covid_info_list[0])
            CovidRepository.extract_case_from_json_list(self, covid_info_list)
            current_date += timedelta(days=7)
        print('all data from united states fetched')
        print('finished day: ' + current_date)
        print('countries list lenght: ' +   str(len(self.countries_json_list)))
        print('cases list count: ' + str(len(self.cases_json_list)))



    def get_country_covid_infos(slug, from_date, to_date):
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


        