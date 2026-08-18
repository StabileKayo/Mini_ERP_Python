from mysql.connector import Error 

class ProdutoRepository:


    def __init__(self, db):
        self.db = db


    def cadastrar(self, nome, preco, estoque):
        sql = """
        INSERT INTO produtos (nome, preco, estoque)
        VALUES (%s, %s, %s)
        """
        valores = (nome, preco, estoque)

        try:
            self.db.cursor.execute(sql,valores)
            self.db.conexao.commit()
        except Error as erro:
            print(f"Erro ao cadastrar produto: {erro}")


    def listar(self):
        try:
            self.db.cursor.execute("""
                SELECT id_produto, nome, preco, estoque
                FROM produtos
                """)
            return self.db.cursor.fetchall()
        
        except Error as erro:
            print(f"Erro ao listar produtos: {erro}")


    def excluir(self, id_produto):
        sql = """
        DELETE FROM produtos
        WHERE id_produto = %s
        """

        try:
            self.db.cursor.execute(sql, (id_produto,))
            self.db.conexao.commit()

            return self.db.cursor.rowcount > 0

        except Error as erro:
            print(f"Erro ao excluir produto: {erro}")
            return False


    def atualizar(self, id_produto, coluna, novo_valor):
        colunas_permitidas = {
            "nome",
            "preco",
            "estoque"
        }
        if coluna not in colunas_permitidas:
            return False

        sql = f"""
        UPDATE produtos
        SET {coluna} = %s
        WHERE id_produto = %s
        """

        try:
            self.db.cursor.execute(
                sql,
                (novo_valor, id_produto)
            )
            self.db.conexao.commit()

            return self.db.cursor.rowcount > 0

        except Error as erro:
            print(f"Erro ao atualizar produto: {erro}")
            return False