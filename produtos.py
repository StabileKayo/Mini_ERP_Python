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
            print(f"Preço: {preco}")
            print(f"Estoque: {estoque}")
    except Error as erro:
        print(f"Erro ao listar produto: {erro}")


def excluir_produto():
    os.system("cls")
    cursor.execute("SELECT id_produto, nome FROM produtos")
    produtos = cursor.fetchall()
    for id_produto, nome in produtos:
        print("-" * 30)
        print(f"Id: {id_produto}")
        print(f"Nome: {nome}")

    id_excluir = input("Digite o Id do produto que quer excluir: ")

    if not id_excluir.isdigit():
        print("Digite um id válido")
        return
    
    sql = "DELETE FROM produtos WHERE id_produto =%s"
    valores = (id_excluir,)

    try:
        cursor.execute(sql, valores)
        conexao.commit()
        if cursor.rowcount > 0:
            print("Produto excluido com sucesso!")
        else:
            print("Nenhum produto com esse Id")
    except Error as erro:
        print(f"Erro ao excluir produto: {erro}")


def atualizar_produto():
    listar_produtos()

    id_atualizar = input("Digite o Id do produto que deseja atualizar: ")

    if not id_atualizar.isdigit():
        print("Digite um id válido")
        return
    print("1 - Nome")
    print("2 - Preço")
    print("3 - Estoque")
    dado_atualizar = input("Digite o que deseja alterar: ")
    if not dado_atualizar.isdigit():
        print("Digite um número")
        return
    dado_atualizar = int(dado_atualizar)

    if dado_atualizar == 1:
        coluna = "nome"
        novo_valor = input("Digite o novo nome: ")
    elif dado_atualizar == 2:
        coluna = "preco"
        novo_valor = input("Digite o novo preço: ")
    elif dado_atualizar == 3:
        coluna = "estoque"
        novo_valor = input("Digite o novo estoque: ")
    else:
        print("Digite um número válido")
        return

    sql = f"UPDATE produtos SET {coluna} = %s WHERE id_produto = %s"
    try:
        cursor.execute(sql, (novo_valor, id_atualizar))
        conexao.commit()
        if cursor.rowcount > 0:
            print("Produto atualizado com sucesso!")
        else:
            print("Nenhum produto com esse Id")
    except Error as erro:
        print(f"Erro ao atualizar produto: {erro}")