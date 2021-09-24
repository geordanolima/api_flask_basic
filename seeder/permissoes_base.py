from permissoes.serializer import SerializerPermissoes


class seeder():
    def __init__(self):
        self.permissoes_base = [
            {'descricao': 'inicio', 'icone': 'home'},
            {'descricao': 'dashboard', 'icone': 'dashboard'},
            {'descricao': 'configurações', 'icone': 'settings'},
            {'descricao': 'usuarios', 'icone': 'users'},
            {'descricao': 'permissoes', 'icone': 'config'},
            {'descricao': 'clientes', 'icone': 'clients'},
            {'descricao': 'vendas', 'icone': 'store'},
            {'descricao': 'produtos', 'icone': 'shopping'}
        ]
        self.permissoes = SerializerPermissoes()
        super().__init__()

    def valida_permissoes_existentes(self):
        return self.permissoes.base.get()

    def cria_permissoes(self):
        if not self.valida_permissoes_existentes():
            print('>>> criando permissoes base')
            for premissao in self.permissoes_base:
                self.permissoes.base.insert(premissao)
