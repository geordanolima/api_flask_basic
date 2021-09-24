import sqlite3
from base.base import SerializerBase


class SerializerPermissoes:

    def __init__(self):
        self.obj_permissao = {
            'id': int,
            'descricao': str,
            'icone': str
        },
        self.base = SerializerBase(tabela='permissoes', obj=self.obj_permissao)
        super().__init__()

    def get_permissao(self, id=None):
        return self.base.get(id=id)

    def insert_permissao(self, permissao):
        return self.base.insert(objeto=permissao)

    def update_permissao(self, permissao, id):
        return self.base.update(objeto=permissao, id=id)

    def delete_permissao(self, id):
        return self.base.delete(pId=id)
