#imports necessarios
from sqlalchemy import create_engine
import pandas as pd
import json 

#fazendo uploads dos arquivos no AWS RDS (Banco)
arquivo = open('teste-lucas.json')
jsons = json.load(arquivo)
json_lista = list(map(lambda x: json.loads(x), jsons))
leitura = pd.DataFrame(json_lista)
#print(leitura)
engine = create_engine('mysql+mysqlconnector://admin:accme159753@accme-database.c8fsb3usjei0.us-east-2.rds.amazonaws.com/accmedatabase')

leitura.to_sql('tb_countries', engine, if_exists='append', index=False)



