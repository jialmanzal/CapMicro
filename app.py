from flask import Flask, Response, json
from database.db import initialize_db
from resources.routes import  inicializar_rutas
from flask_restful import Api
from configparser import ConfigParser

app = Flask(__name__)
api = Api(app)

config = ConfigParser()
config.read('config.properties')

app.config['MONGODB_SETTINGS'] = {
    'host': config.get(section='database_config', option='host')
    + config.get(section='database_config', option='database')
}

@app.route('/')
def base():
    return Response(response=json.dumps({
        "Estado": "OK",
        "base_datos": config.get(section='database_config', option='host')
    }),status=200,
    mimetype='application/json')

initialize_db(app)
inicializar_rutas(api)

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
