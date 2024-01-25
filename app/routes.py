from flask import request
from flask_rdf import flask_rdf
from app import app

@app.route('/api/v1/')
def welcome():
  return "StarChild API v1"

@app.route('/api/v1/users')
@flask_rdf
def user_create():
  # data = graph.serialize(format='turtle').decode('utf-8')
  # return data
