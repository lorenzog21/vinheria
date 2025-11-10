from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/catalogo', methods=['GET'])
def get_catalogo():
    return jsonify({"message": "Serviço de Catálogo ativo", "status": "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
