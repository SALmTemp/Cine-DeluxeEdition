
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from flask import Blueprint, request, jsonify, json

from Model.token import Token, TokenSchema

routes_token = Blueprint("routes_token", __name__)

# token
Token_Schema = TokenSchema()
Token_Schema = TokenSchema(many=True)
