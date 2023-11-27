from config.db import db , ma , app
from flask import Blueprint , render_template,request,jsonify,session

routes_login = Blueprint("routes_login",__name__)

#creamos la ruta del home
@routes_login.route("/indexLogin" , methods=["GET"])
def indexdetails():
    return render_template('/login/login.html')