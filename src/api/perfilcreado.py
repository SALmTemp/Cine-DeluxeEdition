from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from model.perfilcreado import PerfilesCreados, PerfilesCreadosSchema

routes_perfilcreado = Blueprint("routes_perfilcreado", __name__)

# perfil creado
PerfilCreado_Schema = PerfilesCreadosSchema()
PerfilCreado_Schema = PerfilesCreadosSchema(many=True)

