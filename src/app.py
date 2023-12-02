#favor mantener todo organizado
from flask import  redirect, request, jsonify, json, session, render_template
from config.db import  db, app, ma



#Importar los model (Tabla de la base de datos)
#Tener en cuenta el orden de las tabla para las relaciones 







#importar rutas
from rutas.main import routes_main
from rutas.details import routes_details
from rutas.movielist import routes_movielist






#ubicacion del api 








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