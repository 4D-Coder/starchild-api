from flask import Flask
from .routes import starchild
from rdflib_sqlalchemy import registerplugins
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
  SWAGGER_URL,
  API_URL,
  config={
    'app_name': 'StarChild API'
  }
)

def create_app():
  app = Flask(__name__)
  app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
  app.register_blueprint(starchild)
  registerplugins()
  # if __name__ == '__main__':
  #   app.run(debug=True,host="0.0.0.0",port=8080)
  return app




