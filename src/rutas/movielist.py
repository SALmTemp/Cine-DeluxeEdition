from config.db import db , ma , app
from flask import Blueprint , render_template,request,jsonify,session

routes_movielist = Blueprint("routes_movielist",__name__)

#creamos la ruta del home
@routes_movielist.route("/indexmovielist" , methods=["GET"])
def indexmovielist():
    return render_template('/main/movie-list.html')