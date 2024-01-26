from flask import request, Blueprint
from flask_rdf import flask_rdf
from .extensions.graph import build_triple

app = Blueprint("app", __name__)

@app.route('/api/v1/')
def welcome():
  return "StarChild API v1"

@app.route('/api/v1/register', methods=['GET', 'POST'])
@flask_rdf
def user_create():
  build_triple



