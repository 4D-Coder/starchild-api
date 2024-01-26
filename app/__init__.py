from flask import Flask
from rdflib_sqlalchemy import registerplugins

def create_app():
  app = Flask(__name__)

  registerplugins()
  return app
