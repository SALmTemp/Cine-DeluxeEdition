from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from model.userroles import UserRoles, UserRolesSchema

routes_userroles = Blueprint("routes_userroles", __name__)

# userroles
UserRoles_Schema = UserRolesSchema()
UserRoles_Schema = UserRolesSchema(many=True)

@routes_userroles.route('/viewuserroles', methods=['GET'] )
def viewuserroles():
    
    return "Hola userroles"


@routes_userroles.route('/UserRoles', methods=['GET'])
def UserRoles():    
    returnall = UserRoles.query.all()
    resultado_usuarios = UserRoles_Schema.dump(returnall)
    return jsonify(resultado_usuarios)

@routes_userroles.route("/eliminar_UserRoles/<id>", methods=["GET"])
def eliminar_UserRoles(id):
    id_user = UserRoles.query.get(id)
    db.session.delete(id_user)
    db.session.commit()
    return jsonify(UserRolesSchema.dump(id_user))