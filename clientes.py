import os
from database import conexao, cursor
from mysql.connector import Error

def cadastrar_cliente():
    os.system("cls")
    print("---- Cadastro de cliente ----")
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
    valores = (nome, email, telefone)
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("Cliente cadastrado!")
    except Error as erro:
        print(f"Erro ao cadastrar cliente:: {erro}")

def listar_clientes():
    os.system("cls")
    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        print("---- Lista de clientes ----")
        for id_cliente, nome, email, telefone in clientes:
            print("-" * 30)
            print(f"Id: {id_cliente}")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Telefone: {telefone}")
    except Error as erro:
        print(f"Erro ao listar clientes: {erro}")

def excluir_cliente():
    os.system("cls")
    cursor.execute("SELECT id_cliente, nome FROM clientes")
    clientes = cursor.fetchall()
    print("-" * 30)
    for id_cliente, nome in clientes:
        print(f"- Id: {id_cliente} - Nome: {nome}")
    id_excluir = input("Digite o Id do cliente que deseja excluir: ")
    if not id_excluir.isdigit():
        print("Digite um Id válido")
        return
    id_excluir = int(id_excluir)
    sql = "DELETE FROM clientes WHERE id_cliente = %s"
    valores = (id_excluir,)

    try:
        cursor.execute(sql, valores)
        conexao.commit()
        if cursor.rowcount > 0:
            print("Cliente excluido com sucesso!")
        else:
            print("Nenhum cliente com esse Id")
    except Error as erro:
        print(f"Erro ao excluir cliente: {erro}")

def atualizar_cliente():
    listar_clientes()
    id_atualizar = input("Digite o Id do cliente que deseja atualizar: ")
    if not id_atualizar.isdigit():
        print("Digite um Id válido")
        return
    id_atualizar = int(id_atualizar)
    print("1 - Nome")
    print("2 - Email")
    print("3 - Telefone")
    dado_atualizar = input("Digite o dado que você deseja atualizar: ")
    if not dado_atualizar.isdigit():
        print("Digite um número")
        return
    dado_atualizar = int(dado_atualizar)
    if dado_atualizar == 1:
        coluna = "nome" 
        novo_valor = input("Digite o novo nome: ").strip()
        if not novo_valor:
            print("O valor não pode ser vazio.")
            return
    elif dado_atualizar == 2:
        coluna = "email"
        novo_valor = input("Digite o novo email: ")
    elif dado_atualizar == 3:
        coluna = "telefone"
        novo_valor = input("Digite o novo telefone: ")
    else:
        print("Digite um número válido")
        return
    sql = f"UPDATE clientes SET {coluna} = %s WHERE id_cliente = %s"
    try:
        cursor.execute(sql, (novo_valor,id_atualizar))
        conexao.commit()
        if cursor.rowcount > 0:
            print("Cliente atualizado com sucesso!")
        else:
            print("Nenhum cliente com esse Id")
    except Error as erro:
        print(f"Erro ao atualizar cliente: {erro}")