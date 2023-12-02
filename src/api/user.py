from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from model.user import User, UserSchema

routes_user = Blueprint("routes_user", __name__)

# usuario
User_Schema = UserSchema()
User_Schema = UserSchema(many=True)

@routes_user.route('/viewuser', methods=['GET'] )
def viewuser():
    
    return "Hola User"

@routes_user.route('/Usuarios', methods=['GET'])
def usuarios():    
    returnall = User.query.all()
    resultado_usuarios = User_Schema.dump(returnall)
    return jsonify(resultado_usuarios)

@routes_user.route("/eliminar_Users/<id>", methods=["GET"])
def eliminar_users(id):
    id_user = User.query.get(id)
    db.session.delete(id_user)
    db.session.commit()
    return jsonify(UserSchema.dump(id_user))