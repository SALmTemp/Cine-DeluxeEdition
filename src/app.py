#favor mantener todo organizado
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma


#Importar los model (Tabla de la base de datos)
#Tener en cuenta el orden de las tabla para las relaciones 
from api.experiencia import routes_experiencia
from api.perfilcreado import routes_perfilcreado
from api.subcripcion import routes_subcripcion
from api.userroles import routes_userroles
from api.estado import routes_estados
from api.user import routes_user
from api.token import routes_token
from api.cuenta import routes_cuenta








#importar rutas
from rutas.cuentas import routes_Cuentas
from rutas.main import routes_main
from rutas.details import routes_details
from rutas.movielist import routes_movielist






#ubicacion del api 
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_token, url_prefix="/api")
app.register_blueprint(routes_cuenta, url_prefix="/api")
app.register_blueprint(routes_experiencia, url_prefix="/api")
app.register_blueprint(routes_perfilcreado, url_prefix="/api")
app.register_blueprint(routes_subcripcion, url_prefix="/api")
app.register_blueprint(routes_userroles, url_prefix="/api")
app.register_blueprint(routes_estados, url_prefix="/api")








#ubicacion rutas
app.register_blueprint(routes_main, url_prefix="/fronted")
app.register_blueprint(routes_details, url_prefix="/fronted")
app.register_blueprint(routes_movielist, url_prefix="/fronted")



@app.route("/")
def index():
    titulo= "Pagina Principal"
    return render_template('main/index.html', titles=titulo)

@app.route("/algo")
def otr():
    return "hola mondongo"


if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')