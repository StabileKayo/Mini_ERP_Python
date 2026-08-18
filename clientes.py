from mysql.connector import Error


class ClienteRepository:


    def __init__(self, db):
        self.db = db


    def cadastrar(self, nome, email, telefone):
        sql = """
        INSERT INTO clientes (nome, email, telefone)
        VALUES (%s, %s, %s)
        """
        valores = (nome, email, telefone)

        try: 
            self.db.cursor.execute(sql, valores)
            self.db.conexao.commit()

        except Error as erro:
            print(f"Erro ao cadastrar crliente: {erro}")


    def listar(self):
        try:
            self.db.cursor.execute("""
                SELECT id_cliente, nome, email, telefone
                FROM clientes
                """)
            return self.db.cursor.fetchall()
        except Error as erro:
            print(f"Erro ao listar clientes: {erro}")
            return []


    def excluir(self, id_cliente):
        sql = "DELETE FROM clientes WHERE id_cliente = %s"

        try:
            self.db.cursor.execute(sql, (id_cliente,))
            self.db.conexao.commit()

            return self.db.cursor.rowcount > 0

        except Error as erro:
            print(f"Erro ao excluir cliente: {erro}")
            return False


    def atualizar(self, id_cliente, coluna, novo_valor):
        colunas_permitidas = {
            "nome",
            "email",
            "telefone"
        }

        if coluna not in colunas_permitidas:
            return False

        sql = f"""
        UPDATE clientes
        SET {coluna} = %s
        WHERE id_cliente = %s
        """
        try:
            self.db.cursor.execute(
                sql,
                (novo_valor, id_cliente)
            )
            self.db.conexao.commit()
            return self.db.cursor.rowcount > 0
        except Error as erro:
            print(f"Erro ao atualizar cliente: {erro}")
            return False
