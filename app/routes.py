from flask import request, Blueprint
from flask_rdf import flask_rdf
from .graph import create_rdf_graph

main = Blueprint()
@app.route('/api/v1/')
def welcome():
  return "StarChild API v1"

@app.route('/api/v1/users', methods=['GET', 'POST'])
@flask_rdf
def user_create():
  import ipdb; ipdb.set_trace()
  g = create_rdf_graph()
  # data = graph.serialize(format='turtle').decode('utf-8')
  # return data
