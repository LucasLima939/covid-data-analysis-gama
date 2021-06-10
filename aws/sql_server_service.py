import psycopg2
#teste de criação do banco no postgree

class SQLServerService:
    def __init__(self):
        self.conn = psycopg2.connect(host="accme-database.c8fsb3usjei0.us-east-2.rds.amazonaws.com",
                                     database="accme-database",
                                     user="admin",
                                     password="accme159753")

        self.cursor = self.conn.cursor()
        print('----connection ongoing-----')

    # def testConnection(self):
    #    self.cursor.execute('SELECT * FROM tb_historico_filmes')  
    #    print(self.cursor)
    #    for row in self.cursor:
    #        print(row)

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

    # def writeHistory(self):
    #    query = """INSERT INTO articles (nome_filme, data_pesquisa, ano_filme) VALUES (%s, %s, %s);"""
    #    self.cursor.execute(query, ('TESTE2', 2022, ))
    #    self.conn.commit()
    #    self.cursor.execute('SELECT author FROM articles')
    #    rows = self.cursor.fetchall()
    #    print(rows)
