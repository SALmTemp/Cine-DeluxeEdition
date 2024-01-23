from config.db import db , ma , app
from flask import Blueprint , render_template,request,jsonify,session
from model.user import User, UserSchema  
from datetime import datetime, timedelta   
from model.peliculas import Peliculas, PeliculasSchema

routes_details = Blueprint("routes_details",__name__)

#creamos la ruta del home
@routes_details.route("/indexdetails" , methods=["GET"])
def indexdetails():
    return render_template('/main/detail.html')


@routes_details.route('/getmovieurl', methods=['POST'])
def getmovieurl():
    try:
        moviid = request.json.get('moviid')
        print(f"Received request for moviid: {moviid}")

        if moviid is not None:
            pelicula = Peliculas.query.filter_by(moviid=moviid).first()

            if pelicula is not None:
                print(f"Found URL for moviid {moviid}: {pelicula.url}")
                return jsonify({'url': pelicula.url, 'status': 'success', 'exists': True})
        
        print(f"Movie with moviid {moviid} not found")
        return jsonify({'status': 'not_found', 'exists': False})

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'status': 'server_error', 'exists': False}), 500
    



@routes_details.route('/check_token', methods=['POST'])
def check_token():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)

        if user:
            print('Token Expiration:', user.expiration)
            now = datetime.now()
            print('Current Datetime:', now)

            # Asegúrate de ajustar los nombres de las columnas según tu modelo
            if user.token == request.headers.get('Authorization')[7:]:
                if user.is_token_valid():
                    print('Is Token Valid: True')
                    return jsonify({'token_expired': False}), 200

                # Token expired or does not exist, remove it from the user object
                user.token = None
                user.expiration = None
                db.session.commit()  # Confirmar los cambios en la base de datos
                print('Token deleted from user object')

    print('Is Token Valid: False')
    return jsonify({'token_expired': True}), 401
