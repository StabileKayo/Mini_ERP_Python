from database import conexao, cursor
from mysql.connector import Error 

def cadastrar_produto():
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = input("Digite o preço do produto: ")
    estoque_produto = input("Digite quantos desse produto tem no estoque: ")

    sql = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)"
    valores = (nome_produto, preco_produto, estoque_produto)
    try: 
        cursor.execute(sql, valores)
        conexao.commit()
        print("Produto cadastrado com sucesso!")
    except Error as erro:
        print(f"Erro ao cadastrar produto: {erro}")
