from config.db import db , ma , app
from flask import Blueprint , render_template,request,jsonify,session
from model.user import User, UserSchema         

routes_login = Blueprint("routes_login",__name__)

#creamos del registro
@routes_login.route("/indexlogin" , methods=["GET"])
def indexlogin():
    

    return render_template('/main/login.html')

#creamos del registro
@routes_login.route('/login',methods=['POST'])
def login():
    fullemail = request.json['fullemail']
    fullpassword = request.json['fullpassword']
    # Verificar si el usuario y la contraseña son válidos en la base de datos
    user = User.query.filter_by(email=fullemail, password=fullpassword).first()

    if user:
        # Si las credenciales son válidas, inicie sesión al usuario
        session['user_id'] = user.id
        response_body = {'message': 'Inicio de sesión exitoso'}
        status = 200
    else:
        # Si las credenciales no son válidas, envíe un mensaje de error
        response_body = {'message': 'Credenciales inválidas'}
        status = 401
    
    headers = {'Content-Type': 'application/json'}
    return jsonify(response_body), status, headers

