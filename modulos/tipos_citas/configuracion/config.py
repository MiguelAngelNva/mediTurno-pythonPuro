import json 

def cargar_configuracion(path="modulos/tipos_citas/configuracion/config.json"):
    with open(path) as f:
        return json.load(f)