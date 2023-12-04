from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_Cuentas = Blueprint("routes_Cuentas", __name__)
from Model.cuenta import *


@routes_Cuentas.route('/IndexCuentas', methods=['GET'] )
def IndexCuentas():
    
    return render_template('/Main/IndexCuentas.html')