from config.db import db , ma , app
from flask import Blueprint , render_template,request,jsonify,session

routes_login = Blueprint("routes_login",__name__)

#creamos del registro
@routes_login.route("/indexlogin" , methods=["GET"])
def indexlogin():
    return render_template('/main/login.html')