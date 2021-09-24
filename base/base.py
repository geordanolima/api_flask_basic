import sqlite3
from bd import BD

banco = BD()


class SerializerBase:
    def __init__(self, tabela: str, obj: object):
        self.tabela = tabela
        self.obj = obj
        super().__init__()

    def _get_list_obj(self):
        retorno = []
        for item in self.obj[0].items():
            retorno.append({item[0]: item[1]})
        return retorno

    def _define_select(self, id=None, filtro=None):
        select = 'SELECT * FROM {tabela}'.format(tabela=self.tabela)
        if filtro:
            return '{select} WHERE {filtro}'.format(select=select, filtro=filtro)
        return select if not id else '{select} WHERE id = {id}'.format(select=select, id=id)

    def _define_delete(self, id: int):
        return 'DELETE FROM {tabela} WHERE id = {id}'.format(tabela=self.tabela, id=id)

    def _define_insert(self, objeto: object):
        monta_insert = self._get_list_obj()
        insert = 'INSERT INTO {tabela} ('.format(tabela=self.tabela)
        for i in monta_insert:
            if list(i.items())[0][0] == 'id':
                continue
            insert += '{chave},'.format(chave=list(i.items())[0][0])
        insert = insert[:-1] + ') VALUES ('
        for i in monta_insert:
            if list(i.items())[0][0] == 'id':
                continue
            insert += '"{valor}",'.format(valor=objeto.get(list(i.items())[0][0]))
        insert = insert[:-1] + ')'
        return insert

    def _define_update(self, objeto: object, id: int):
        monta_update = self._get_list_obj()
        update = 'UPDATE {tabela} SET '.format(tabela=self.tabela)
        for i in monta_update:
            if list(i.items())[0][0] == 'id':
                continue
            update += '{chave}="{valor}", '.format(
                chave=list(i.items())[0][0],
                valor=objeto.get(list(i.items())[0][0])
            )
        update = '{update} WHERE id = "{id}"'.format(update=update[:-2], id=id)
        return update

    def _executa_script(self, script: str, id=None, get=True):
        retorno = {}
        try:
            conn = banco.connect_to_db()
            cur = conn.cursor()
            cur.execute(script)
            conn.commit()
            if get:
                retorno = self.get(id=id if id else cur.lastrowid)
        except Exception as erro:
            conn.rollback()
            return {}, erro
        finally:
            conn.close()
        return retorno

    def get(self, id=None, filtro=None):
        retorno = []
        monta_objeto = self._get_list_obj()
        try:
            conn = banco.connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(self._define_select(id=id, filtro=filtro))
            rows = cur.fetchall()
            objeto = {}
            for item in rows:
                for i in monta_objeto:
                    objeto.setdefault(list(i.items())[0][0], list(i.items())[0][1](item[list(i.items())[0][0]]))
                retorno.append(objeto)
                objeto = {}
        except Exception as erro:
            retorno = []
        return retorno if not id else retorno[0]

    def insert(self, objeto: object):
        return self._executa_script(script=self._define_insert(objeto=objeto))

    def update(self, objeto: object, id: int):
        return self._executa_script(script=self._define_update(objeto=objeto, id=id), id=id)

    def delete(self, id: int):
        deleta, erro = self._executa_script(script=self._define_delete(id=id), id=id, get=False)
        if not erro:
            return '{tabela} deletado com sucesso'.format(tabela=self.tabela)
        return 'erro ao deletar {tabela}. {erro}'.format(tabela=self.tabela, erro=erro)
