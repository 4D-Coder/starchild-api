from app import app
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Game Information API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
  app.run(debug=True,host="0.0.0.0",port=8080)
