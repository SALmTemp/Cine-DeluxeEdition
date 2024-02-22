from config.db import db , ma , app
from flask import Blueprint , render_template,request,jsonify,session
from model.user import User, UserSchema  
import secrets
from datetime import datetime, timedelta    

routes_login = Blueprint("routes_login",__name__)

#creamos del registro
@routes_login.route("/indexlogin" , methods=["GET"])
def indexlogin():
    

    return render_template('/main/login.html')

# #creamos del registro
# @routes_login.route('/login', methods=['POST'])
# def login():
#     fullemail = request.json.get('fullemail')  # Usa get para evitar excepciones si la clave no está presente
#     fullpassword = request.json.get('fullpassword')

#     # Verificar si el usuario y la contraseña son válidos en la base de datos
#     user = User.query.filter_by(email=fullemail, password=fullpassword).first()

#     if user:
#         # Obtener el id del usuario
#         user_id = user.id

#         # Verificar si el usuario ya tiene un token existente
#         if user.token:
#             # Si ya tiene un token, actualiza el token existente
#             user.token = secrets.token_urlsafe(32)
#             user.expiration = datetime.now() + timedelta(minutes=30)
#             user.ip = request.remote_addr
#             user.dispositivo = request.user_agent.string
#         else:
#             # Si no tiene un token, crea uno nuevo
#             new_token = secrets.token_urlsafe(32)

#             # Asignar los valores del token al usuario
#             user.token = new_token
#             user.expiration = datetime.now() + timedelta(minutes=30)
#             user.ip = request.remote_addr
#             user.dispositivo = request.user_agent.string

#         # Commit de la sesión
#         db.session.commit()

#         # Iniciar sesión al usuario
#         session['user_id'] = user_id

#         response_body = {'message': 'Inicio de sesión exitoso', 'token': user.token}
#         status = 200
#     else:
#         # Si las credenciales no son válidas, envíe un mensaje de error
#         response_body = {'message': 'Credenciales inválidas'}
#         status = 401
    
#     headers = {'Content-Type': 'application/json'}
#     return jsonify(response_body), status, headers



