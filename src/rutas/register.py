from config.db import db , ma , app
from datetime import datetime, timezone, timedelta
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import ssl
from email.message import EmailMessage
from flask import Blueprint , render_template,request,jsonify,session
from sqlalchemy.exc import IntegrityError
from model.user import User, UserSchema 
from model.subcripcion import Subcripcion
from model.estado import Estados
from model.experiencia import Experiencia
from model.perfilcreado import PerfilesCreados
from model.userroles import UserRoles

routes_register = Blueprint("routes_register",__name__)

#creamos la ruta del home
@routes_register.route("/indexregister" , methods=["GET"])
def indexregister():
    return render_template('/main/register.html')


@routes_register.route('/forgotpassword', methods=['POST'])
def forgotpassword():
    fullcorreo = request.json['fullcorreo']

    # Check if the user has exceeded the request limit
    now = datetime.now(timezone.utc)
    elapsed_time = timedelta(minutes=5)
    request_count = 0

    if 'last_request_time' in session and 'request_count' in session:
        last_request_time = session['last_request_time']
        request_count = session['request_count']
        elapsed_time = now - last_request_time

        # Calculate the time remaining until the limit resets
        time_to_wait = timedelta(minutes=5 + (request_count - 1)) - elapsed_time
        hours = time_to_wait.seconds // 3600
        minutes = (time_to_wait.seconds % 3600) // 60
        seconds = time_to_wait.seconds % 60

        if elapsed_time < timedelta(minutes=5 + (request_count - 1)) and request_count >= 5:
            return jsonify({'message': f'Too many requests. Please try again in {hours} hour(s), {minutes} minute(s), and {seconds} second(s).', 'time_to_wait': time_to_wait.total_seconds()}), 429

    # No necesitas consultar la base de datos para verificar la existencia del correo electrónico

    # Genera un código de verificación basado en el hash del correo electrónico
    code_list = random.sample(range(10), 4)
    code = ''.join(str(digit) for digit in code_list)

    # Guarda el código en la sesión
    session['verification_code'] = code

    # Crea el mensaje de correo electrónico con diseño personalizado
    subject = 'Stremovify Verification Code'

    # Logo y nombre ficticio
    logo_url = 'https://example.com/logo.png'
    my_name = 'StreMovify'

    # Diseño degradado en azul y morado
    body = f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: 'Arial', sans-serif;
                        text-align: center;
                        margin: 0;
                        padding: 0;
                        background: linear-gradient(to right, #0a0a0a, #1f1735);
                    }}
                    .container {{
                        width: 80%;
                        margin: 0 auto;
                        background-color: rgba(255, 255, 255, 0.9);
                        padding: 20px;
                        border-radius: 10px;
                        margin-top: 50px;
                        text-align: center;
                    }}
                    .header {{
                        text-align: center;
                    }}
                    .header img {{
                        max-width: 100px;
                    }}
                    .content {{
                        padding: 20px;
                        color: #2f084d;
                        text-align: center;
                    }}
                    h2 {{
                        color: #4d43d6;
                    }}
                    p {{
                        line-height: 1.6;
                    }}
                    strong {{
                        color: #e50914;
                    }}
                    .footer {{
                        text-align: center;
                        color: #555;
                        margin-top: 20px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <img src="{logo_url}" alt="Stremovify Logo">
                        <h2>{subject}</h2>
                    </div>
                    <div class="content">
                        <p>Dear Stremovify User,</p>
                         <p>¡Hola!
                         ¡Te damos la bienvenida a Netflix! Nos encanta que estés aquí. Completa la suscripción para empezar a ver las series y películas de las que todo el mundo habla. Los planes comienzan desde $ 16.900 al mes.</p>
                         <p>¿Todavía tienes dudas sobre cómo funciona Netflix?
                         Entretenimiento ilimitado.Ve todo lo que quieras a un precio accesible.Cancela cuando quieras.Sin contratos ni compromisos.Recomendaciones exclusivas para ti.Encuentra siempre una serie o película para ver según tus gustos
                        <p>Esperamos que este correo electrónico te encuentre bien. Como parte de nuestro compromiso con la seguridad, hemos iniciado un proceso de verificación para su cuenta..</p>
                        <p>Your verification code is: <strong>{code}</strong></p>
                        <p>Utilice este código para completar el proceso de verificación. Si no solicitó este código, ignore este correo electrónico.</p>
                        <p>Te enviamos este email porque creaste una cuenta de Netflix, pero no completaste la suscripción. Si no quieres recibir estos emails.</p>
                        <p>For further assistance or information, feel free to reach out to our support team.</p>
                        
                    </div>
                    <div class="footer">
                        <p>Best regards,<br>{my_name}</p>
                    </div>
                </div>
            </body>
        </html>
    """

    # Envía el correo electrónico al usuario con el código
    sender_email = 'stremovify@gmail.com'
    sender_password = 'ovkblgkretkotakw'
    receiver_email = fullcorreo

    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'html'))
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    # Reinicia el contador de solicitudes si ha pasado el tiempo
    if elapsed_time >= timedelta(minutes=5 + (request_count - 1)):
        session['request_count'] = 1
    else:
        # Actualiza la sesión con el contador de solicitudes y la última hora de solicitud
        session['request_count'] = session.get('request_count', 0) + 1
    session['last_request_time'] = now

    return jsonify({'message': 'Verification code sent.'})

@routes_register.route('/verificarcode', methods=['POST'])
def verificarcode():
    
    verification_code = request.json['verification_code']
    stored_code = session.get('verification_code')
    
    if verification_code == stored_code:
        # Si el código es correcto, redireccionar al usuario a la página de cambio de contraseña
        response_body = {'message': 'Código verificado correctamente'}
        status = 200
        session.pop('verification_code', None)
        return jsonify(response_body), status
    else:
        # Si el código no es correcto, devolver un error
        response_body = {'message': 'El código ingresado es incorrecto. Inténtalo de nuevo.'}
        status = 401
        return jsonify(response_body), status
    
#Registrar
@routes_register.route('/saveUsuarios', methods=['POST'])
def saveUsuariosrg():
    try:
        username = request.json['username']
        fullname = request.json['fullname']
        correo = request.json['correo']
        contrasena = request.json['contrasena']
        format = request.json['format']
        
        print('\n',format, username, fullname, correo, contrasena,'\n')
        # Crea una nueva instancia de User
        new_user = User( id_subcripcion=int(format), id_estado=2, id_experiencia=2, id_perfilescreados=2, id_usersroles=3, username=username, email=correo, password=contrasena, fullname=fullname, registration=datetime.now())

        # Agrega las instancias a la sesión y realiza la transacción
        db.session.add(new_user)
        db.session.commit()
        
        # Si las credenciales son válidas, inicie sesión al usuario
        return {
            "status": 200,
            "message": "Inicio de sesión exitoso",
            "nombre_usuario": username  # Incluir el nombre del administrador en la respuesta
        }
        
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Error de integridad de la llave foránea"}), 400
