from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vino-secret-key'

# Login simples que gera token JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data and data.get('username') == 'admin' and data.get('password') == '123':
        token = jwt.encode(
            {'user': data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return jsonify({'token': token})
    return jsonify({'message': 'Credenciais inválidas'}), 401

# Endpoint protegido
@app.route('/usuarios', methods=['GET'])
def get_users():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token ausente'}), 403
    try:
        decoded = jwt.decode(token.split(" ")[1], app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'message': f'Serviço de Usuários ativo para {decoded["user"]}'})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token expirado'}), 401
    except:
        return jsonify({'message': 'Token inválido'}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
