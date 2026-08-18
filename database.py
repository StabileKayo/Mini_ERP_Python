import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            self.conexao = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "mini_erp"
            )
            self.cursor = self.conexao.cursor()
        except Error as erro:
            print(f"Erro ao conectar ao banco: {erro}")
            raise