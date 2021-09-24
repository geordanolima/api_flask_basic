import bcrypt
import sqlite3
from permissoes.serializer import SerializerPermissoes
from permissoes_usuario.serializer import SerializerPermissoesUsuario
from base.base import SerializerBase


class SerializerUsuario:

    def __init__(self):
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
        self.base = SerializerBase(tabela='usuarios', obj=self.obj_usuario)
        self.salt = bcrypt.gensalt(6)
        self.serializer_permissoes = SerializerPermissoes()
        self.serializer_permissoes_usuario = SerializerPermissoesUsuario()
        super().__init__()

    def get_usuario(self, id=None):
        return self.base.get(id=id)

    def insert_usuario(self, usuario):
        usuario['senha'] = bcrypt.hashpw(usuario['senha'].encode('utf8'), self.salt).decode()
        usuario_retorno = self.base.insert(objeto=usuario)
        usuario_retorno['permissoes'] = self._cria_permissoes_usuario(usuario_retorno.get('id'))
        return usuario_retorno

    def update_usuario(self, usuario, id):
        return self.base.update(objeto=usuario, id=id)

    def delete_usuario(self, id):
        return self.base.delete(pId=id)

    def efetuar_login(self, usuario):
        filtro = 'usuario="{usuario}"'.format(usuario=usuario.get('usuario'))
        _usuario = self.base.get(filtro=filtro)[0]
        if bcrypt.checkpw(usuario.get('senha').encode('utf8'), _usuario.get('senha').encode()):
            _usuario['token'] = ''
            return _usuario
        raise {'erro': 'autenticação incorreta'}

    def _cria_permissoes_usuario(self, id):
        permissoes_criadas = []
        for permissao in self.serializer_permissoes.get_permissao():
            obj_permissao = {
                'id_usuario': id,
                'descricao': permissao.get('descricao'),
                'icone': permissao.get('icone'),
                'habilita': True
            }
            permissoes_criadas.append(self.serializer_permissoes_usuario.insert_permissao(obj_permissao))
        return permissoes_criadas
