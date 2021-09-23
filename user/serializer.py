import sqlite3
from bd import BD
from base.base import SerializerBase

banco = BD()


class SerializerUsuario:

    def __init__(self):
        self.base = SerializerBase()
        self.obj_usuario = {
            'id': int,
            'nome': str,
            'usuario': str,
            'senha': str,
            'email': str,
            'telefone': str,
            'celular': str,
            'foto': str
        },
        self.tabela = 'usuarios'
        self.INSERT_USUARIO = 'INSERT INTO usuarios (nome, usuario, senha, email, telefone, celular, foto) \
            VALUES ("{nome}", "{usuario}", "{senha}", "{email}", "{telefone}", "{celular}", "{foto}")'
        self.UPDATE_USUARIO = 'UPDATE usuarios SET nome="{nome}", usuario="{usuario}", senha="{senha}", \
            email="{email}", telefone="{telefone}", celular="{celular}", foto="{foto}" WHERE id ={id}'
        super().__init__()

    def get_users(self, id=None):
        return self.base.get(pTabela=self.tabela, pObj=self.obj_usuario, pId=id)

    def insert_user(self, user):
        return self.base.insert(
            pScript=self.INSERT_USUARIO.format(
                nome=user.get('nome', ''),
                usuario=user.get('usuario', ''),
                senha=user.get('senha', ''),
                email=user.get('email', ''),
                telefone=user.get('telefone', ''),
                celular=user.get('celular', ''),
                foto=user.get('foto', '')
            ),
            pObj=self.obj_usuario,
            pTabela=self.tabela
        )

    def update_user(self, user, id):
        return self.base.update(
            pScript=self.UPDATE_USUARIO.format(
                nome=user.get('nome', ''),
                usuario=user.get('usuario', ''),
                senha=user.get('senha', ''),
                email=user.get('email', ''),
                telefone=user.get('telefone', ''),
                celular=user.get('celular', ''),
                foto=user.get('foto', ''),
                id=id
            ),
            pId=id,
            pObj=self.obj_usuario,
            pTabela=self.tabela
        )

    def delete_user(self, id):
        return self.base.delete(pId=id, pTabela=self.tabela)
