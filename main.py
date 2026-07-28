from clientes import (
    cadastrar_cliente,
    listar_clientes,
    excluir_cliente,
    atualizar_cliente,
)

SAIR = 5

ESCOLHAS = {
    1: cadastrar_cliente,
    2: listar_clientes,
    3: excluir_cliente,
    4: atualizar_cliente,
}


def exibir_menu():
    print("-------- MENU --------")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Excluir cliente")
    print("4 - Atualizar cliente")
    print("5 - Sair")


def main():
    while True:
        exibir_menu()
        escolha = input("Escolha: ")

        if not escolha.isdigit():
            print("Digite um número válido")
            continue

        escolha = int(escolha)

        if escolha == SAIR:
            break

        if escolha not in ESCOLHAS:
            print("Digite um número válido")
            continue

        ESCOLHAS[escolha]()


if __name__ == "__main__":
    main()
