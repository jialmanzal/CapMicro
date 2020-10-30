from flask import Response, request
from database.cuentamedica import CuentaMedica
from flask_restful import Resource

class CuentaMedicaAPI(Resource):
    def get(self):
        cuentaMedica = CuentaMedica.objects.to_json()
        return Response(cuentaMedica, mimetype='application/json', status=200)

    def post(self):
        body = request.get_json()
        cuentaMedica = CuentaMedica(**body).save()
        id = cuentaMedica.id
        return {'id': str(id)}, 200
