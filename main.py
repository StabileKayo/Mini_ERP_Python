from clientes import (
    cadastrar_cliente, 
    listar_clientes, 
    excluir_cliente,
    atualizar_cliente
    )
from produtos import(
    cadastrar_produto
)


def menu_clientes():
    print("-------- MENU --------")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Excluir cliente")
    print("4 - Atualizar cliente")
    print("5 - Voltar")

    escolha = input("Escolha: ")

    if not escolha.isdigit():
        print("Digite um número ")
        return True
    
    escolha = int(escolha)

    if escolha == 5:
        return False
    elif escolha == 1:
        cadastrar_cliente()
    elif escolha == 2:
        listar_clientes()
    elif escolha == 3:
        excluir_cliente()
    elif escolha == 4:
        atualizar_cliente()        
    else:
        print("Digite um número válido")
    return True  


def menu_produtos():
    print("-------- MENU --------")
    print("1 - Cadastrar produto")
    print("2 - Voltar")

    escolha = input("Escolha: ")

    if not escolha.isdigit():
        print("Digite um número ")
        return True

    escolha = int(escolha)

    if escolha == 2:
        return False
    if escolha == 1:
        cadastrar_produto()


while True:
    print("-------- MENU --------")
    print("1 - Menu Cliente")
    print("2 - Menu Produto")
    print("3 - Sair")

    escolha = input("Escolha: ")
    if not escolha.isdigit():
        print("Digite um número")
        continue

    escolha = int(escolha)

    if escolha == 3:
        break
    elif escolha == 1:
        menu_clientes()
    elif escolha == 2:
        menu_produtos()
    else:
        print("Digite um número válido")
        continue