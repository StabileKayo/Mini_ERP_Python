import os
from database import conexao, cursor


def cadastrar_cliente():
    os.system("cls")
    print("---- Cadastro de cliente ----")
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
    valores = (nome, email, telefone)

    cursor.execute(sql, valores)
    conexao.commit()
    print("Cliente cadastrado!")


def listar_clientes():
    os.system("cls")
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    print("---- Lista de clientes ----")
    for id_cliente, nome, email, telefone in clientes:
        print("-" * 30)
        print(f"Id: {id_cliente}")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"Telefone: {telefone}")


def excluir_cliente():
    os.system("cls")
    cursor.execute("SELECT id_cliente, nome FROM clientes")
    clientes = cursor.fetchall()
    for id_cliente, nome in clientes:
        print("-" * 30)
        print(f"Id: {id_cliente}")
        print(f"Nome: {nome}")
    id_excluir = input("Digite o ID do cliente que deseja excluir: ")
    if not id_excluir.isdigit():
        print("Digite um Id válido")
        return
    id_excluir = int(id_excluir)
    sql = "DELETE FROM clientes WHERE id_cliente = %s"
    valores = (id_excluir,)

    cursor.execute(sql, valores)
    conexao.commit()
    if cursor.rowcount > 0:
        print("Cliente excluido com sucesso!")
    else:
        print("Nenhum cliente com esse Id")
