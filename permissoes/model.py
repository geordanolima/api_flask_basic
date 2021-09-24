
def createTablePermissoes():
    return '''
        CREATE TABLE permissoes (
            id INTEGER PRIMARY KEY NOT NULL,
            descricao TEXT NOT NULL,
            icone TEXT NOT NULL
        );
    '''
