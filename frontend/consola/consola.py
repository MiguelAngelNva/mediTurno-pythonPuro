import requests
import json

MODULOS = {
    "comentarios": "modulos/comentarios/configuracion/config.json",
    "medicos": "modulos/medicos/configuracion/config.json",
    "ciudades": "modulos/ciudades/configuracion/config.json",
    "documentos": "modulos/documentos/configuracion/config.json",
    "estados": "modulos/estados/configuracion/config.json",
    "pacientes": "modulos/pacientes/configuracion/config.json",
    "sedes": "modulos/sedes/configuracion/config.json",
    "citas": "modulos/citas/configuracion/config.json",
    "notificadores": "modulos/notificadores/configuracion/config.json",
    "especialidades": "modulos/especialidades/configuracion/config.json",
    "medico_especialidad": "modulos/medico_especialidad/configuracion/config.json",
    "tipos_citas": "modulos/tipos_citas/configuracion/config.json"
}

def cargar_endpoints_desde_config(path):
    with open(path) as f:
        config = json.load(f)
    return config["api_base"], config["endpoints"]

def menu_general():
    print("\n===== Selección de módulo =====")
    for idx, nombre in enumerate(MODULOS.keys(), start=1):
        print(f"{idx}. {nombre.capitalize()}")
    print(f"{len(MODULOS)+1}. Salir")

def menu_operaciones():
    print("\n===== Operaciones =====")
    print("1. Crear")
    print("2. Listar")
    print("3. Obtener por ID")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Volver")

def crear(api, endpoint):
    datos = {}
    print("\nIngrese los datos en formato clave=valor (vacío para terminar):")
    while True:
        linea = input("> ")
        if not linea.strip():
            break
        if "=" not in linea:
            print("Formato inválido, usa clave=valor")
            continue
        clave, valor = linea.split("=", 1)
        datos[clave.strip()] = valor.strip()
    r = requests.post(f"{api}{endpoint['create']}", json=datos)
    print(r.json())

def listar(api, endpoint):
    r = requests.get(f"{api}{endpoint['read_all']}")
    for item in r.json():
        print(item)

def obtener(api, endpoint):
    id = input("ID: ")
    url = endpoint["read_one"].replace("{id}", id)
    r = requests.get(f"{api}{url}")
    print(r.json() if r.status_code == 200 else "No encontrado.")

def actualizar(api, endpoint):
    id = input("ID a actualizar: ")
    url = endpoint["update"].replace("{id}", id)
    datos = {}
    print("Ingrese los nuevos datos en formato clave=valor (vacío para terminar):")
    while True:
        linea = input("> ")
        if not linea.strip():
            break
        if "=" not in linea:
            print("Formato inválido, usa clave=valor")
            continue
        clave, valor = linea.split("=", 1)
        datos[clave.strip()] = valor.strip()
    r = requests.put(f"{api}{url}", json=datos)
    print(r.json())

def eliminar(api, endpoint):
    id = input("ID a eliminar: ")
    url = endpoint["delete"].replace("{id}", id)
    r = requests.delete(f"{api}{url}")
    print(r.json())

if __name__ == "__main__":
    while True:
        menu_general()
        seleccion = input("Selecciona un módulo: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(MODULOS):
            modulo = list(MODULOS.keys())[int(seleccion)-1]
            ruta_config = MODULOS[modulo]
            try:
                api, endpoint = cargar_endpoints_desde_config(ruta_config)
            except FileNotFoundError:
                print(f"No se encontró el archivo de configuración para {modulo}")
                continue

            while True:
                menu_operaciones()
                op = input("Operación: ")
                if op == "1": crear(api, endpoint)
                elif op == "2": listar(api, endpoint)
                elif op == "3": obtener(api, endpoint)
                elif op == "4": actualizar(api, endpoint)
                elif op == "5": eliminar(api, endpoint)
                elif op == "6": break
                else: print("Opción inválida.")
        elif seleccion == str(len(MODULOS)+1):
            print("Saliendo del sistema")
            break
        else:
            print("Módulo inválido.")