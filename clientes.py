from database import conexao, cursor


def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
    valores = (nome, email, telefone)

    cursor.execute(sql, valores)
    conexao.commit()
    print("Cliente cadastrado!")