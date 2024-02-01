import flask_rdf
from flask import request, Blueprint
from .extensions.graph import build_triple
from .models.dataclasses import User

starchild = Blueprint("starchild", __name__)

@starchild.route('/api/v1/')
def welcome():
  return "StarChild API v1"

# @flask_rdf
@starchild.route('/api/v1/register', methods=['GET', 'POST'])
def register():
  match request.method:
    case 'Post':
      params = get_params(request)
      user = User()
    case 'GET':
      pass



def get_params(request):
  return request.get_json()
