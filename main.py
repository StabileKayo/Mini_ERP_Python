while True:
    print("----- MENU -----")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Sair")
    escolha = input("Escolha: ")
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:
            pass
        elif escolha == 2:
            pass
        elif escolha == 3:
            break
        else:
            print("Digite um número válido")
            continue
    else:
        print("Digite um número")
        continue