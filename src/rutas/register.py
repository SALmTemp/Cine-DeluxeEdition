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

from model.user import User, UserSchema

routes_register = Blueprint("routes_register",__name__)

#creamos la ruta del home
@routes_register.route("/indexregister" , methods=["GET"])
def indexregister():
    return render_template('/main/register.html')


@routes_register.route('/forgotpassword', methods=['POST'])
def forgotpassword():
    fullcorreo = request.json['fullcorreo']

    # Check if the user has exceeded the request limit
    now = datetime.now(timezone.utc)  # Convert to offset-aware datetime in UTC
    elapsed_time = timedelta(minutes=5)  # Valor predeterminado de 5 minutos
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

    # Envía un correo electrónico al usuario con el código
    sender_email = 'bytvflix@gmail.com'
    sender_password = 'eawkyimzkehbpgbm'
    receiver_email = fullcorreo
    message = f'Subject: Verification Code\n\nYour verification code is: {code}'
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

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
    
