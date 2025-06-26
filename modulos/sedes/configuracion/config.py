import json 

def cargar_configuracion(path="modulos/sedes/configuracion/config.json"):
    with open(path) as f:
        return json.load(f)