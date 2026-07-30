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
from pedidos import(
    cadastrar_pedido,
)


VOLTAR = 5
SAIR = 4

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

ESCOLHAS_PEDIDO = {
    1: cadastrar_pedido
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


def menu_pedidos():
    print("-------- MENU --------")
    print("1 - Cadastrar pedido")
    print("2 - Voltar")

    escolha = input("Escolha: ")

    if not escolha.isdigit():
        print("Digite um número ")
        return True

    escolha = int(escolha)

    if escolha == 2:
        return False
    if escolha not in ESCOLHAS_PEDIDO:
        print("Digite um número válido")
        return True
    ESCOLHAS_PEDIDO[escolha]()


while True:
    print("-------- MENU --------")
    print("1 - Clientes")
    print("2 - Produtos")
    print("3 - Pedidos")
    print("4 - Sair")

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
    elif escolha == 3:
        menu_pedidos()
    else:
        print("Digite um número válido")
        continue