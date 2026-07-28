import mysql.connector
from mysql.connector import Error
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mini_erp"
    )
    cursor = conexao.cursor()

except Error as erro:
    print(f"Erro ao conectar ao banco: {erro}")
    exit()