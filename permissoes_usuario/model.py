
def createTablePermissoesUsuario():
    return '''
        CREATE TABLE permissoes_usuario (
            id INTEGER PRIMARY KEY NOT NULL,
            id_usuario INTEGER NOT NULL,
            descricao TEXT NOT NULL,
            icone TEXT NOT NULL,
            habilita NUMERIC NOT NULL,
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
        );
    '''
