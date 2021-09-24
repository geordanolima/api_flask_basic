#!/usr/bin/python
import sqlite3
from usuarios.model import createTableCliente
from permissoes.model import createTablePermissoes
from permissoes_usuario.model import createTablePermissoesUsuario


class BD():
    def __init__(self):
        self.db_name = 'banco.db'
        self.create_db_tables()
        super().__init__()

    def connect_to_db(self):
        conn = sqlite3.connect(self.db_name)
        return conn

    def create_db_tables(self):
        try:
            conn = self.connect_to_db()
            conn.execute(createTableCliente())
            conn.execute(createTablePermissoes())
            conn.execute(createTablePermissoesUsuario())
            conn.commit()
            print("tabelas criadas com sucesso")
        except Exception as erro:
            print("falha ao criar tabela no banco: {}".format(erro))
        finally:
            conn.close()
