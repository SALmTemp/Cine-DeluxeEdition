from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from model.experiencia import Experiencia, ExperienciasSchema

routes_experiencia = Blueprint("routes_experiencia", __name__)

# subcripcion
Experiencia_Schema = ExperienciasSchema()
Experiencia_Schema = ExperienciasSchema(many=True)

@routes_experiencia.route('/viewExperiencia', methods=['GET'] )
def viewExperiencia():
    
    return "Hola Experiencia"

@routes_experiencia.route('/experiencia', methods=['GET'])
def experiencia():    
    returnall = Experiencia.query.all()
    resultado_usuarios = Experiencia_Schema.dump(returnall)
    return jsonify(resultado_usuarios)

@routes_experiencia.route("/eliminar_experiencia/<id>", methods=["GET"])
def eliminar_experiencia(id):
    id_user = Experiencia.query.get(id)
    db.session.delete(id_user)
    db.session.commit()
    return jsonify(ExperienciasSchema.dump(id_user))