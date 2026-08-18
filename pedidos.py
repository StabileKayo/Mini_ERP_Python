from mysql.connector import Error

class PedidoRepository:

    def __init__(self, db):
        self.db = db

    def cadastrar(self, id_cliente):
        sql = """
        INSERT INTO pedidos (id_cliente)
        VALUES (%s)
        """

        try:
            self.db.cursor.execute(sql, (id_cliente,))
            self.db.conexao.commit()

            return True

        except Error as erro:
            print(f"Erro ao criar pedido: {erro}")
            return False


    def listar(self):
        try:
            sql = """
            SELECT
                p.id_pedido,
                c.nome,
                p.data_pedido
            FROM pedidos p
            INNER JOIN clientes c
                ON p.id_cliente = c.id_cliente
            """

            self.db.cursor.execute(sql)
            return self.db.cursor.fetchall()
        
        except Error as erro:
            print(f"Erro ao listar pedidos: {erro}")
            return []


    def excluir(self, id_pedido):
        sql = """
        DELETE FROM pedidos
        WHERE id_pedido = %s
        """

        try:
            self.db.cursor.execute(sql, (id_pedido,))
            self.db.conexao.commit()

            return self.db.cursor.rowcount > 0
        
        except Error as erro:
            print(f"Erro ao excluir pedido: {erro}")
            return False