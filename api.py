from flask import Flask, request, jsonify
from flask_cors import CORS
from user.serializer import SerializerUsuario

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
usuario = SerializerUsuario()


@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(usuario.get_users())


@app.route('/api/users/<id>', methods=['GET'])
def api_get_user(id):
    return jsonify(usuario.get_users(id))


@app.route('/api/users', methods=['POST'])
def api_add_user():
    return jsonify(usuario.insert_user(request.get_json()))


@app.route('/api/users/<id>', methods=['PUT'])
def api_update_user(id):
    return jsonify(usuario.update_user(request.get_json(), id))


@app.route('/api/users/<id>', methods=['DELETE'])
def api_delete_user(id):
    return jsonify(usuario.delete_user(id))


if __name__ == "__main__":
    # app.debug = True
    # app.run(debug=True)
    app.run()  # run app
