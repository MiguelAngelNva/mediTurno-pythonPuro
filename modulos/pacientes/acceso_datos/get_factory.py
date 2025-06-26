from modulos.pacientes.configuracion.config import cargar_configuracion
from modulos.pacientes.acceso_datos.mysql_factory import MySQLPacienteDAOFactory
from modulos.pacientes.acceso_datos.postgres_factory import PostgresPacienteDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresPacienteDAOFactory()
    return MySQLPacienteDAOFactory()