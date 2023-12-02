from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from model.subcripcion import Subcripcion, SubcripcionSchema

routes_subcripcion = Blueprint("routes_subcripcion", __name__)

# subcripcion
Subcripcion_Schema = SubcripcionSchema()
Subcripcion_Schema = SubcripcionSchema(many=True)

@routes_subcripcion.route('/viewsubcripcion', methods=['GET'] )
def viewsubcripcion():
    
    return "Hola Subcripcion"

@routes_subcripcion.route('/Subcripcion', methods=['GET'])
def Subcripcion():    
    returnall = Subcripcion.query.all()
    resultado_usuarios = Subcripcion_Schema.dump(returnall)
    return jsonify(resultado_usuarios)

@routes_subcripcion.route("/eliminar_Subcripcion/<id>", methods=["GET"])
def eliminar_Subcripcion(id):
    id_user = Subcripcion.query.get(id)
    db.session.delete(id_user)
    db.session.commit()
    return jsonify(SubcripcionSchema.dump(id_user))