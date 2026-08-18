from mysql.connector import Error

class ItemPedidoRepository:

    def __init__(self,db):
        self.db = db


    def adicionar(self, id_pedido, id_produto, quantidade):
        try:
            sql = """
            SELECT preco
            FROM produtos
            WHERE id_produto = %s
            """

            self.db.cursor.execute(sql, (id_produto,))
            resultado = self.db.cursor.fetchone()

            if resultado is None:
                return False

            preco = resultado[0]

            sql = """
            INSERT INTO itens_pedido
            (id_pedido, id_produto, quantidade, preco_unitario)
            VALUES (%s, %s, %s, %s)
            """

            valores = (
                id_pedido,
                id_produto,
                quantidade,
                preco
            )

            self.db.cursor.execute(sql, valores)
            self.db.conexao.commit()

            return True

        except Error as erro:
            print(f"Erro ao adicionar item ao pedido: {erro}")
            return False