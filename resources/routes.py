from .CuentaMedicaAPI import CuentaMedicaAPI

def inicializar_rutas(api):
    api.add_resource(CuentaMedicaAPI, '/api/cuentamedica')