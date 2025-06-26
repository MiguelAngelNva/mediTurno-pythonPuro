from modulos.estados.configuracion.config import cargar_configuracion
from modulos.estados.acceso_datos.mysql_factory import MySQLEstadoDAOFactory
from modulos.estados.acceso_datos.postgres_factory import PostgresEstadoDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresEstadoDAOFactory()
    return MySQLEstadoDAOFactory()