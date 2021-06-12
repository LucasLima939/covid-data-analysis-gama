import psycopg2
import pandas as pd
from sqlalchemy import create_engine

class SQLServerService:
    def __init__(self):
        self.conn = create_engine('mysql+mysqlconnector://admin:accme159753@accme-database.c8fsb3usjei0.us-east-2.rds.amazonaws.com/accmedatabase')


        #self.cursor = self.conn.cursor()

    #def testConnection(self):
    #    self.cursor.execute('SELECT * FROM tb_historico_filmes')  
    #    print(self.cursor)
    #    for row in self.cursor:
    #        print(row)
    def read_data(self, sql_query):
        print('carregando dados...')
        response = pd.read_sql(sql_query, con=self.conn)
        print('dados carregados!')
        print('------------------------')
        print(response)
        print('------------------------')

    def createCountriesTable(self):
        query = """CREATE TABLE tb_countries(
            id SERIAL PRIMARY KEY,
            country_name VARCHAR(255),
            country_code VARCHAR(2),
            lat VARCHAR(10),
            lon VARCHAR(10)
        )"""
        self.cursor.execute(query)
        self.conn.commit()

    def createCasesTable(self):
        query = """CREATE TABLE tb_cases(
            id SERIAL PRIMARY KEY,
            confirmed INTEGER,
            deaths INTEGER,
            actives INTEGER,
            recovered INTEGER,
            date TIMESTAMP,
            country_id INTEGER,
            FOREIGN KEY(country_id) REFERENCES tb_countries(id)
        )"""
        self.cursor.execute(query)
        self.conn.commit()

    #def writeHistory(self):
    #    query = """INSERT INTO articles (nome_filme, data_pesquisa, ano_filme) VALUES (%s, %s, %s);"""
    #    self.cursor.execute(query, ('TESTE2', 2022, ))
    #    self.conn.commit()
    #    self.cursor.execute('SELECT author FROM articles')
    #    rows = self.cursor.fetchall()
    #    print(rows)