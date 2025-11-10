from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def get_users():
    return jsonify({"message": "Serviço de Usuários ativo", "status": "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
