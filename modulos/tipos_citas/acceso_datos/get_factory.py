from modulos.medicos.configuracion.config import cargar_configuracion
from modulos.medicos.acceso_datos.mysql_factory import MySQLMedicoDAOFactory
from modulos.medicos.acceso_datos.postgres_factory import PostgresMedicoDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresMedicoDAOFactory()
    return MySQLMedicoDAOFactory()