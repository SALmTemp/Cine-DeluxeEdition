from config.db import db , ma , app
from flask import Blueprint , render_template,request,jsonify,session

routes_details = Blueprint("routes_details",__name__)

#creamos la ruta del home
@routes_details.route("/indexdetails" , methods=["GET"])
def indexdetails():
    return render_template('/main/detail.html')