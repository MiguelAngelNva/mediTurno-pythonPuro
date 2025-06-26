import json 

def cargar_configuracion(path="modulos/medico_especialidad/configuracion/config.json"):
    with open(path) as f:
        return json.load(f)