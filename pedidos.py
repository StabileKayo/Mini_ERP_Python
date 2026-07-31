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
        sql = "INSERT INTO pedidos (id_cliente) VALUES (%s)"
        cursor.execute(sql, (id_cliente,))
        conexao.commit()

        print("Pedido criado com sucesso!")

    except Error as erro:
        print(f"Erro ao criar pedido: {erro}")


def listar_pedidos():
    os.system("cls")
    try:
        sql = """SELECT
        p.id_pedido,
        c.nome,
        p.data_pedido
        FROM pedidos p
        INNER JOIN clientes c
        ON p.id_cliente = c.id_cliente;
        """
        cursor.execute(sql)
        pedidos = cursor.fetchall()

        if not pedidos: 
            print("Nenhum pedido cadastrado.")
            return

        print("---- Lista de pedidos ----")
        for id_pedido, nome, data_pedido in pedidos:
            print(f"Id: {id_pedido} - {nome} - {data_pedido}")

    except Error as erro:
        print(f"Erro ao listar pedido: {erro}")


def excluir_pedido():
    os.system("cls")
    listar_pedidos()
    id_excluir = input("Digite o Id do pedido que deseja excluir: ")
    if not id_excluir.isdigit():
        print("Digite um número válido")
        return
    id_excluir = int(id_excluir)
    sql = "DELETE FROM pedidos WHERE id_pedido = %s"
    valores = (id_excluir,)

    try:
        cursor.execute(sql, valores)
        conexao.commit()
        if cursor.rowcount > 0:
            print("Pedido excluido com sucesso")
        else:
            print("Nenhum pedido com esse Id")

    except Error as erro:
        print(f"Erro ao excluir pedido: {erro}")