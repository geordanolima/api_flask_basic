#!/usr/bin/python
import sqlite3
from user.model import createTableCliente


class BD():
    def __init__(self):
        self.create_db_tables()
        super().__init__()

    def connect_to_db(self):
        conn = sqlite3.connect('database.db')
        return conn

    def create_db_tables(self):
        try:
            conn = self.connect_to_db()
            conn.execute(createTableCliente())
            conn.commit()
            print("tabelas criadas com sucesso")
        except Exception as erro:
            print("falha ao criar tabela no banco: {}".format(erro))
        finally:
            conn.close()
