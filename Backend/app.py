from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from decouple import config


# Obtener los valores de las variables de entorno
mongo_host = config('MONGO_HOST')
mongo_port = config('MONGO_PORT')



print(mongo_host)

app = Flask(__name__)
app.config['MONGO_URI'] = f"mongodb://{mongo_host}:{mongo_port}/donto"

mongo = PyMongo(app)
db = mongo.db.users
@app.route('/login', methods=['POST'])
def login():
    # Obtener los datos enviados en la solicitud
    data = request.get_json()

    # Extraer el correo electrónico y la contraseña del usuario
    email = data.get('email')
    password = data.get('password')

    # Aquí puedes agregar la lógica de autenticación o cualquier otro procesamiento necesario

    # Ejemplo de verificación básica: si el correo y la contraseña no están vacíos
    if email and password:
        # Realizar las acciones necesarias, como verificar las credenciales en una base de datos
        # o generar un token de acceso para el usuario
        user = {
            'email': email,
            'password': password
        }
        id = db.insert_one(user).inserted_id
        # Ejemplo de respuesta exitosa
        response = {
            'message': 'Login successful',
            'user': {
                '_id': str(id)
            }
        }
        print(response)
        return jsonify(response), 200
    else:
        # Ejemplo de respuesta de error si faltan datos
        response = {
            'message': 'Invalid request. Email and password are required.'
        }
        return jsonify(response), 400
@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'Accediendo a la API'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
