from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from Model.perfilcreado import PerfilesCreados, PerfilesCreadosSchema

routes_perfilcreado = Blueprint("routes_perfilcreado", __name__)

# perfil creado
PerfilCreado_Schema = PerfilesCreadosSchema()
PerfilCreado_Schema = PerfilesCreadosSchema(many=True)

@routes_perfilcreado.route('/viewperfilcreado', methods=['GET'] )
def viewperfilcreado():
    
    return "Hola Perfil Creado"

@routes_perfilcreado.route('/PerfilCreado', methods=['GET'])
def PerfilCreado():    
    returnall = PerfilesCreados.query.all()
    resultado_usuarios = PerfilCreado_Schema.dump(returnall)
    return jsonify(resultado_usuarios)

@routes_perfilcreado.route("/eliminar_perfilcreado/<id>", methods=["GET"])
def eliminar_perfilcreado(id):
    id_user = PerfilesCreados.query.get(id)
    db.session.delete(id_user)
    db.session.commit()
    return jsonify(PerfilesCreadosSchema.dump(id_user))