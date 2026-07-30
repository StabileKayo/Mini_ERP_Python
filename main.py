from clientes import (
    cadastrar_cliente, 
    listar_clientes, 
    excluir_cliente,
    atualizar_cliente
    )
from produtos import(
    cadastrar_produto,
    listar_produtos,
    excluir_produto,
    atualizar_produto
)

VOLTAR = 5
SAIR = 3

ESCOLHAS_CLIENTE = {
    1: cadastrar_cliente,
    2: listar_clientes,
    3: excluir_cliente,
    4: atualizar_cliente
}

ESCOLHAS_PRODUTO = {
    1: cadastrar_produto,
    2: listar_produtos,
    3: excluir_produto,
    4: atualizar_produto
}


def menu_clientes():
    print("-------- MENU --------")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Excluir cliente")
    print("4 - Atualizar cliente")
    print("5 - Voltar")

    escolha = input("Escolha: ")

    if not escolha.isdigit():
        print("Digite um número válido")
        return True
    
    escolha = int(escolha)

    if escolha == VOLTAR:
        return False
    if escolha not in ESCOLHAS_CLIENTE:
        print("Digite um número válido")
        return True  
    ESCOLHAS_CLIENTE[escolha]()


def menu_produtos():
    print("-------- MENU --------")
    print("1 - Cadastrar produto")
    print("2 - Listar produto")
    print("3 - Excluir produto")
    print("4 - Atualizar produto")
    print("5 - Voltar")

    escolha = input("Escolha: ")

    if not escolha.isdigit():
        print("Digite um número ")
        return True

    escolha = int(escolha)

    if escolha == VOLTAR:
        return False
    if escolha not in ESCOLHAS_PRODUTO:
        print("Digite um número válido")
        return True
    ESCOLHAS_PRODUTO[escolha]()


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

    if escolha == SAIR:
        break
    elif escolha == 1:
        menu_clientes()
    elif escolha == 2:
        menu_produtos()
    else:
        print("Digite um número válido")
        continue