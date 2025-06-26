import json 

def cargar_configuracion(path="modulos/estados/configuracion/config.json"):
    with open(path) as f:
        return json.load(f)