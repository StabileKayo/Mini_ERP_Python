import os
from database import conexao, cursor
from mysql.connector import Error 


def cadastrar_pedido():
    os.system("cls")

    try:
        cursor.execute("SELECT id_cliente, nome FROM clientes")
        clientes = cursor.fetchall()

        print("---- Clientes ----")

        for id_cliente, nome in clientes:
            print(f"{id_cliente} - {nome}" )

        id_cliente = input("Digite o Id do cliente: ")

        if not id_cliente.isdigit():
            print("Digite um Id válido")
            return
        sql = """
        INSERT INTO PEDIDOS (id_cliente)
        VALUES (%s)
        """
        cursor.execute(sql, (id_cliente,))
        conexao.commit()

        print("Pedido criado com sucesso!")

    except Error as erro:
        print(f"Erro ao criar pedido: {erro}")

