from sqlalchemy import create_engine
import sqlalchemy as sql

class EngineBRAZ:
    def __init__(self):
        self.DRIVER = "ODBC Driver 17 for SQL Server"
        self.USERNAME = "admin"
        self.PSSWD = "14253679"
        self.SERVERNAME = "database-1.cx0qiyqyuurd.us-east-1.rds.amazonaws.com"
        self.INSTANCENAME = ""
    
    def GenEngine(self,db):
        self.engine_server = sql.create_engine(
            f"mssql+pyodbc://{self.USERNAME}:{self.PSSWD}@{self.SERVERNAME}{self.INSTANCENAME}/{db}?driver={self.DRIVER}", fast_executemany=True
        )
        print(f'Engine criado no Banco de Dados - {db} (SQL Server)')

        return self.engine_server

engine = EngineBRAZ()
