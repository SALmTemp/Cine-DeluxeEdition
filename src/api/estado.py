from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from model.estado import Estados, EstadosSchema

routes_estados = Blueprint("routes_estados", __name__)

# subcripcion
Estado_Schema = EstadosSchema()
Estado_Schema = EstadosSchema(many=True)

@routes_estados.route('/viewEstado', methods=['GET'] )
def viewEstado():
    
    return "Hola Estado"


@routes_estados.route('/estado', methods=['GET'])
def estado():    
    returnall = Estados.query.all()
    resultado_usuarios = Estado_Schema.dump(returnall)
    return jsonify(resultado_usuarios)

@routes_estados.route("/eliminar_estado/<id>", methods=["GET"])
def eliminar_estado(id):
    id_user = Estados.query.get(id)
    db.session.delete(id_user)
    db.session.commit()
    return jsonify(EstadosSchema.dump(id_user))