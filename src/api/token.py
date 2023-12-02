from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from model.token import Token, TokenSchema

routes_token = Blueprint("routes_token", __name__)

# token
Token_Schema = TokenSchema()
Token_Schema = TokenSchema(many=True)

@routes_token.route('/viewtoken', methods=['GET'] )
def viewtoken():
    
    return "Hola cuenta"

@routes_token.route('/Token', methods=['GET'])
def Token():    
    returnall = Token.query.all()
    resultado_usuarios = Token_Schema.dump(returnall)
    return jsonify(resultado_usuarios)

@routes_token.route("/eliminar_Token/<id>", methods=["GET"])
def eliminar_Token(id):
    id_user = Token.query.get(id)
    db.session.delete(id_user)
    db.session.commit()
    return jsonify(TokenSchema.dump(id_user))