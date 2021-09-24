from flask import Flask, request, jsonify
from flask_cors import CORS
from usuarios.serializer import SerializerUsuario
from permissoes_usuario.serializer import SerializerPermissoesUsuario

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
usuario = SerializerUsuario()
permissoes = SerializerPermissoesUsuario()


# usuarios


@app.route('/api/usuario', methods=['GET'])
@app.route('/api/usuario/<id>', methods=['GET'])
def api_get_usuario(id=None):
    return jsonify(usuario.get_usuario(id))


@app.route('/api/usuario', methods=['POST'])
def api_add_usuario():
    return jsonify(usuario.insert_usuario(request.get_json()))


@app.route('/api/usuario/login', methods=['POST'])
def api_login_usuario():
    return jsonify(usuario.efetuar_login(request.get_json()))


@app.route('/api/usuario/<id>', methods=['PUT'])
def api_update_usuario(id):
    return jsonify(usuario.update_usuario(request.get_json(), id))


@app.route('/api/usuario/<id>', methods=['DELETE'])
def api_delete_usuario(id):
    return jsonify(usuario.delete_usuario(id))

# permissoes


@app.route('/api/permissao', methods=['GET'])
@app.route('/api/permissao/<id>', methods=['GET'])
def api_get_permissao(id=None):
    return jsonify(permissoes.get_permissao(id))


@app.route('/api/permissao', methods=['POST'])
def api_add_permissao():
    return jsonify(permissoes.insert_permissao(request.get_json()))


@app.route('/api/permissao/<id>', methods=['PUT'])
def api_update_permissao(id):
    return jsonify(permissoes.update_permissao(request.get_json(), id))


@app.route('/api/permissao/<id>', methods=['DELETE'])
def api_delete_permissao(id):
    return jsonify(permissoes.delete_permissao(id))


if __name__ == "__main__":
    from seeder.permissoes_base import seeder
    seed = seeder()
    seed.cria_permissoes()
    app.run()
