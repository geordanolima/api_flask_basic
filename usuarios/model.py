
def createTableCliente():
    return '''
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY NOT NULL,
            nome TEXT,
            usuario TEXT,
            senha TEXT,
            email TEXT,
            telefone TEXT,
            celular TEXT,
            foto TEXT
        );
    '''
