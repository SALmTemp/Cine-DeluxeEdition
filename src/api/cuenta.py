from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from model.cuenta import Cuentas, CuentasSchema

routes_cuenta = Blueprint("routes_cuenta", __name__)

# cuenta
Cuenta_Schema = CuentasSchema()
Cuenta_Schema = CuentasSchema(many=True)

@routes_cuenta.route('/viewcuenta', methods=['GET'] )
def viewcuenta():
    
    return "Hola cuenta"

@routes_cuenta.route('/Cuenta', methods=['GET'])
def Cuenta():    
    returnall = Cuentas.query.all()
    resultado_usuarios = Cuenta_Schema.dump(returnall)
    return jsonify(resultado_usuarios)

@routes_cuenta.route("/eliminar_cuenta/<id>", methods=["GET"])
def eliminar_cuenta(id):
    id_user = Cuentas.query.get(id)
    db.session.delete(id_user)
    db.session.commit()
    return jsonify(CuentasSchema.dump(id_user))