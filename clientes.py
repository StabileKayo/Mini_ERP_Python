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


def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    for id_cliente, nome, email, telefone in clientes:
        print(f"Id: {id_cliente}")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"Telefone: {telefone}")