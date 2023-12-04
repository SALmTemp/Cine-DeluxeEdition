#favor mantener todo organizado
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma


#Importar los model (Tabla de la base de datos)
#Tener en cuenta el orden de las tabla para las relaciones
from api.experiencia import routes_experiencia
from api.cuenta import routes_cuenta
from api.estado import routes_estados
from api.subcripcion import routes_subcripcion
from api.userroles import routes_userroles
from api.token import routes_token
from api.perfilcreado import routes_perfilcreado
from api.user import routes_user


















#importar rutas
from rutas.cuentas import routes_Cuentas
from rutas.main import routes_main
from rutas.details import routes_details
from rutas.movielist import routes_movielist
from rutas.registromain import routes_RegistroMain
from rutas.login import routes_login
from rutas.register import routes_register
from rutas.profile import routes_profile






#ubicacion del api 
app.register_blueprint(routes_experiencia, url_prefix="/api")
app.register_blueprint(routes_perfilcreado, url_prefix="/api")
app.register_blueprint(routes_subcripcion, url_prefix="/api")
app.register_blueprint(routes_userroles, url_prefix="/api")
app.register_blueprint(routes_estados, url_prefix="/api")
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_token, url_prefix="/api")
app.register_blueprint(routes_cuenta, url_prefix="/api")









#ubicacion rutas
app.register_blueprint(routes_main, url_prefix="/fronted")
app.register_blueprint(routes_details, url_prefix="/fronted")
app.register_blueprint(routes_movielist, url_prefix="/fronted")
app.register_blueprint(routes_RegistroMain, url_prefix="/fronted")
app.register_blueprint(routes_login, url_prefix="/fronted")
app.register_blueprint(routes_register, url_prefix="/fronted")
app.register_blueprint(routes_profile, url_prefix="/fronted")



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