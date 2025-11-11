from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/catalogo', methods=['GET'])
def get_catalogo():
    try:
        # Login no serviço de usuários para obter o token JWT
        auth = requests.post('http://usuarios.vino.local:5000/login', json={'username': 'admin', 'password': '123'})
        token = auth.json().get('token')

        # Usa o token para acessar o endpoint protegido
        headers = {'Authorization': f'Bearer {token}'}
        r = requests.get('http://usuarios.vino.local:5000/usuarios', headers=headers)

        return jsonify({
            'message': 'Serviço de Catálogo ativo e autenticado',
            'usuarios_response': r.json()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
