from Classes.alchemyBRAZ import engine
import pandas as pd
import os
_dir = os.path.dirname(__file__)

def envio_sql(_dir):

    files = os.listdir(fr"{_dir}\Engenheiro de Dados - CSV")
    for file in files:
        
        df = pd.read_csv(fr'{_dir}\Engenheiro de Dados - CSV\{file}',sep = ';', engine = 'python', encoding='utf-8', index_col=False)
        table_name = f"{str(file).rstrip('.csv')}"
  
        print (table_name)
        con_fast = engine.GenEngine('Test-Data Engineer')
        df.to_sql(f'{table_name}', con_fast, if_exists = 'replace', chunksize = 100000, index = False)

        print(f"{table_name} - Envio realizado para o banco de dados")

envio_sql(_dir)