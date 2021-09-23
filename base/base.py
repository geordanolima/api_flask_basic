import sqlite3
from bd import BD

banco = BD()


class SerializerBase:
    def __init__(self):
        self.SELECT_BASE = 'SELECT * FROM {tabela}'
        self.SELECT_ID_BASE = 'SELECT * FROM {tabela} where id = {id}'
        self.DELETE_BASE = 'DELETE FROM {tabela} WHERE id = {id}'
        super().__init__()

    def _get_list_obj(self, pObj: object):
        retorno = []
        for item in pObj[0].items():
            retorno.append({item[0]: item[1]})
        return retorno

    def get(self, pTabela: str, pObj: object, pId=None):
        retorno = []
        monta_objeto = self._get_list_obj(pObj)
        try:
            conn = banco.connect_to_db()
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute((self.SELECT_BASE if not pId else self.SELECT_ID_BASE).format(tabela=pTabela, id=pId))
            rows = cur.fetchall()
            objeto = {}
            for item in rows:
                for i in monta_objeto:
                    objeto.setdefault(list(i.items())[0][0], list(i.items())[0][1](item[list(i.items())[0][0]]))
                retorno.append(objeto)
                objeto = {}
        except Exception as erro:
            retorno = []
        return retorno if not pId else retorno[0]

    def insert(self, pScript: str, pObj: object, pTabela: str):
        inserted_obj = {}
        try:
            conn = banco.connect_to_db()
            cur = conn.cursor()
            cur.execute(pScript)
            conn.commit()
            inserted_obj = self.get(
                pTabela=pTabela,
                pObj=pObj,
                pId=cur.lastrowid
            )
        except Exception as erro:
            print(erro)
            conn().rollback()
        finally:
            conn.close()
        return inserted_obj

    def update(self, pScript: str, pId: int, pObj: object, pTabela: str):
        updated_obj = {}
        try:
            conn = banco.connect_to_db()
            cur = conn.cursor()
            cur.execute(pScript)
            conn.commit()
            updated_obj = self.get(
                pTabela=pTabela,
                pObj=pObj,
                pId=pId
            )
        except Exception:
            conn.rollback()
            updated_obj = {}
        finally:
            conn.close()
        return updated_obj

    def delete(self, pId: int, pTabela: str):
        message = {}
        try:
            conn = banco.connect_to_db()
            conn.execute(self.DELETE_BASE.format(tabela=pTabela, id=pId))
            conn.commit()
            message['status'] = '{} deletado com sucesso'.format(pTabela)
        except Exception:
            conn.rollback()
            message['status'] = 'erro ao deletar {}'.format(pTabela)
        finally:
            conn.close()
        return message
