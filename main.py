from service.sql_server_service import SQLServerService

def main():
    print('init service')
    service = SQLServerService()
    print('test service')
    service.createCountriesTable()
    print('created countries table')
    service.createCasesTable()
    print('created cases table')

main()


    