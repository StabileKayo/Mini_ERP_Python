from clientes import (cadastrar_cliente, listar_clientes, excluir_cliente)

while True:
    print("-------- MENU --------")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Excluir cliente")
    print("4 - Sair")

    escolha = input("Escolha: ")
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:
            cadastrar_cliente()
        elif escolha == 2:
            listar_clientes()
        elif escolha == 3:
            excluir_cliente()
        elif escolha == 4:
            break
        else:
            print("Digite um número válido")
            continue
    else:
        print("Digite um número")
        continue