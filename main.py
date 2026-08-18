from database import Database
from clientes import ClienteRepository
from produtos import ProdutoRepository
from pedidos import PedidoRepository
from itens_pedido import ItemPedidoRepository

db = Database()


cliente_repository = ClienteRepository(db)
produto_repository = ProdutoRepository(db)
pedido_repository = PedidoRepository(db)
item_pedido_repository = ItemPedidoRepository(db)


VOLTAR = 5
SAIR = 5


def menu_clientes():

    while True:
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
            break
        if escolha == 1:
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")

            cliente_repository.cadastrar(
                nome,
                email,
                telefone
            )

        elif escolha == 2:
            clientes = cliente_repository.listar()

            if not clientes:
                print("Nenhum cliente cadastrado.")
                continue

            print("---- Lista de clientes ----")

            for id_cliente, nome, email, telefone in clientes:
                print("-" * 30)
                print(f"Id: {id_cliente}")
                print(f"Nome: {nome}")
                print(f"Email: {email}")
                print(f"Telefone: {telefone}")

        elif escolha == 3:
            id_cliente = input("Digite o Id do cliente que deseja excluir: ")

            if not id_cliente.isdigit():
                print("Digite um Id válido")
                continue

            sucesso = cliente_repository.excluir(int(id_cliente))

            if sucesso:
                print("Cliente excluído com sucesso!")
            else:
                print("Nenhum cliente com esse Id.")
                return

        elif escolha == 4:
            id_cliente = input("Digite o Id do cliente que deseja atualizar: ")

            if not id_cliente.isdigit():
                print("Digite um Id válido")
                continue

            print("1 - Nome")
            print("2 - Email")
            print("3 - Telefone")

            escolha_dado = input("Escolha: ")

            if not escolha_dado.isdigit():
                print("Digite um número válido")
                continue

            escolha_dado = int(escolha_dado)

            colunas = {
                1: "nome",
                2: "email",
                3: "telefone"
            }
            if escolha_dado not in colunas:
                print("Digite uma opção válida")
                continue

            coluna = colunas[escolha_dado]
            novo_valor = input("Digite o novo valor: ")

            sucesso = cliente_repository.atualizar(
                int(id_cliente),
                coluna,
                novo_valor
            )
            if sucesso:
                print("Cliente atualizado com sucesso!")
            else:
                print("Nenhum cliente com esse Id.")
        else:
            print("Digite um número válido")

def menu_produtos():

    while True:
        print("-------- MENU PRODUTOS --------")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Excluir produto")
        print("4 - Atualizar produto")
        print("5 - Voltar")

        escolha = input("Escolha: ")

        if not escolha.isdigit():
            print("Digite um número válido")
            continue

        escolha = int(escolha)

        if escolha == VOLTAR:
            break

        if escolha == 1:
            nome = input("Nome do produto: ")
            preco = input("Preço: ")
            estoque = input("Estoque: ")

            produto_repository.cadastrar(
                nome,
                preco,
                estoque
            )

        elif escolha == 2:
            produtos = produto_repository.listar()

            if not produtos:
                print("Nenhum produto cadastrado.")
                continue

            print("---- Lista de produtos ----")

            for id_produto, nome, preco, estoque in produtos:
                print("-" * 30)
                print(f"Id: {id_produto}")
                print(f"Nome: {nome}")
                print(f"Preço: {preco}")
                print(f"Estoque: {estoque}")

        elif escolha == 3:
            id_produto = input(
                "Digite o Id do produto que deseja excluir: "
            )

            if not id_produto.isdigit():
                print("Digite um Id válido")
                continue

            sucesso = produto_repository.excluir(
                int(id_produto)
            )

            if sucesso:
                print("Produto excluído com sucesso!")
            else:
                print("Nenhum produto encontrado com esse Id.")

        elif escolha == 4:
            id_produto = input(
                "Digite o Id do produto que deseja atualizar: "
            )

            if not id_produto.isdigit():
                print("Digite um Id válido")
                continue

            print("1 - Nome")
            print("2 - Preço")
            print("3 - Estoque")

            escolha_dado = input("Escolha: ")

            if not escolha_dado.isdigit():
                print("Digite um número válido")
                continue

            escolha_dado = int(escolha_dado)

            colunas = {
                1: "nome",
                2: "preco",
                3: "estoque"
            }

            if escolha_dado not in colunas:
                print("Digite uma opção válida")
                continue

            coluna = colunas[escolha_dado]
            novo_valor = input("Digite o novo valor: ")

            sucesso = produto_repository.atualizar(
                int(id_produto),
                coluna,
                novo_valor
            )

            if sucesso:
                print("Produto atualizado com sucesso!")
            else:
                print("Nenhum produto encontrado com esse Id.")

        else:
            print("Digite um número válido")


def menu_pedidos():

    while True:
        print("-------- MENU PEDIDOS --------")
        print("1 - Cadastrar pedido")
        print("2 - Listar pedidos")
        print("3 - Excluir pedido")
        print("4 - Voltar")

        escolha = input("Escolha: ")

        if not escolha.isdigit():
            print("Digite um número válido")
            continue

        escolha = int(escolha)

        if escolha == 4:
            break

        if escolha == 1:
            clientes = cliente_repository.listar()

            if not clientes:
                print("Nenhum cliente cadastrado.")
                continue

            print("---- Clientes ----")

            for id_cliente, nome, email, telefone in clientes:
                print(f"{id_cliente} - {nome}")

            id_cliente = input("Digite o Id do cliente: ")

            if not id_cliente.isdigit():
                print("Digite um Id válido")
                continue

            sucesso = pedido_repository.cadastrar(
                int(id_cliente)
            )

            if sucesso:
                print("Pedido criado com sucesso!")

        elif escolha == 2:
            pedidos = pedido_repository.listar()

            if not pedidos:
                print("Nenhum pedido cadastrado.")
                continue

            print("---- Lista de pedidos ----")

            for id_pedido, nome, data_pedido in pedidos:
                print(
                    f"Id: {id_pedido} - "
                    f"Cliente: {nome} - "
                    f"Data: {data_pedido}"
                )

        elif escolha == 3:
            id_pedido = input(
                "Digite o Id do pedido que deseja excluir: "
            )

            if not id_pedido.isdigit():
                print("Digite um Id válido")
                continue

            sucesso = pedido_repository.excluir(
                int(id_pedido)
            )

            if sucesso:
                print("Pedido excluído com sucesso!")
            else:
                print("Nenhum pedido encontrado com esse Id.")

        else:
            print("Digite um número válido")


def menu_itens():

    while True:
        print("-------- ITENS DO PEDIDO --------")
        print("1 - Adicionar item ao pedido")
        print("2 - Voltar")

        escolha = input("Escolha: ")

        if not escolha.isdigit():
            print("Digite um número válido")
            continue

        escolha = int(escolha)

        if escolha == 2:
            break

        if escolha == 1:

            pedidos = pedido_repository.listar()

            if not pedidos:
                print("Nenhum pedido cadastrado.")
                continue

            print("---- Pedidos ----")

            for id_pedido, nome, data_pedido in pedidos:
                print(
                    f"Id: {id_pedido} - "
                    f"Cliente: {nome} - "
                    f"Data: {data_pedido}"
                )

            id_pedido = input("Digite o Id do pedido: ")

            if not id_pedido.isdigit():
                print("Digite um Id válido")
                continue

            produtos = produto_repository.listar()

            if not produtos:
                print("Nenhum produto cadastrado.")
                continue

            print("---- Produtos ----")

            for id_produto, nome, preco, estoque in produtos:
                print(
                    f"Id: {id_produto} - "
                    f"{nome} - "
                    f"R$ {preco} - "
                    f"Estoque: {estoque}"
                )

            id_produto = input("Digite o Id do produto: ")

            if not id_produto.isdigit():
                print("Digite um Id válido")
                continue

            quantidade = input("Digite a quantidade: ")

            if not quantidade.isdigit():
                print("Digite uma quantidade válida")
                continue

            quantidade = int(quantidade)

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
                continue

            sucesso = item_pedido_repository.adicionar(
                int(id_pedido),
                int(id_produto),
                quantidade
            )

            if sucesso:
                print("Item adicionado ao pedido com sucesso!")

        else:
            print("Digite um número válido")


while True:
    print("-------- MENU --------")
    print("1 - Menu Clientes")
    print("2 - Menu Produtos")
    print("3 - Menu Pedidos")
    print("4 - Menu Itens do pedido")
    print("5 - Sair")

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
    elif escolha == 4:
        menu_itens()
    else:
        print("Digite um número válido")
    