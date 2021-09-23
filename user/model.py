
def createTableCliente():
    return '''
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            celular TEXT NOT NULL,
            foto TEXT NOT NULL
        );
    '''
