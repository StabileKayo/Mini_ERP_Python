import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mini_erp"
)

cursor = conexao.cursor()