import os
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


def listar_produtos():
    os.system("cls")
    try:
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        print("---- Lista de produtos ----")
        for id_produto, nome, preco, estoque in produtos:
            print("-" * 30)
            print(f"Id: {id_produto}")
            print(f"Nome: {nome}")
            print(f"Email: {preco}")
            print(f"Telefone: {estoque}")
    except Error as erro:
        print(f"Erro ao listar clientes: {erro}")