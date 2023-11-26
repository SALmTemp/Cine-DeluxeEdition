from config.db import db , ma , app
from flask import Blueprint , render_template,request,jsonify,session

routes_main = Blueprint("routes_main",__name__)

#creamos la ruta del home
@routes_main.route("/indexmain" , methods=["GET"])
def indexmain():
    return render_template('/main/index.html')