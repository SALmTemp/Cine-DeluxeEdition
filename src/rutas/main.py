from config.db import db , ma , app
from flask import Blueprint , render_template,request,jsonify,session
from model.user import User, UserSchema
from datetime import datetime, timedelta

routes_main = Blueprint("routes_main",__name__)

#creamos la ruta del home
@routes_main.route("/indexmain" , methods=["GET"])
def indexmain():
    return render_template('/main/index.html')

# @routes_main.route('/check_token', methods=['POST'])
# def check_token():
#     user_id = session.get('user_id')
#     if user_id:
#         user = User.query.get(user_id)

#         if user:
#             print('Token Expiration:', user.expiration)
#             now = datetime.now()
#             print('Current Datetime:', now)

#             # Asegúrate de ajustar los nombres de las columnas según tu modelo
#             if user.token == request.headers.get('Authorization')[7:]:
#                 if user.is_token_valid():
#                     print('Is Token Valid: True')
#                     return jsonify({'token_expired': False}), 200

#                 # Token expired or does not exist, remove it from the user object
#                 user.token = None
#                 user.expiration = None
#                 db.session.commit()  # Confirmar los cambios en la base de datos
#                 print('Token deleted from user object')

#     print('Is Token Valid: False')
#     return jsonify({'token_expired': True}), 401