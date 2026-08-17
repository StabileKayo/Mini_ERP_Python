import os
from mysql.connector import Error

from database import conexao, cursor
from pedidos import listar_pedidos
from produtos import listar_produtos


def adicionar_item():
    os.system("cls")

    listar_pedidos()

    id_pedido = input("Digite o Id do pedido: ")
    if not id_pedido.isdigit():
        print("Digite um Id válido")
        return
    id_pedido = int(id_pedido)
    listar_produtos()
    id_produto = input("Digite o Id do produto: ")

    if not id_produto.isdigit():
        print("Digite um Id válido")
        return

    id_produto = int(id_produto)

    quantidade = input("Digite a quantidade: ")

    if not quantidade.isdigit():
        print("Digite uma quantidade válida")
        return
    quantidade = int(quantidade)

    if quantidade <= 0:
        print(" A quantidade deve ser maior que zero")
        return

    try:
        sql = """
        SELECT preco
        FROM produtos
        WHERE id_produto = %s
        """
        cursor.execute(sql, (id_produto,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Nenhum produto encontrado com esse Id")
            return
        preco = resultado[0]

        sql = """
        INSERT INTO itens_pedido
        (id_pedido, id_produto, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s)
        """
        valores = (
            id_pedido,
            id_produto,
            quantidade,
            preco
        )
        cursor.execute(sql, valores)
        conexao.commit()
        print("Item adicionado ao pedido com sucesso!")

    except Error as erro:
        print(f"Erro ao adicionar item ao pedido: {erro}")
