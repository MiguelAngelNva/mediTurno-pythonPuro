from modulos.sedes.configuracion.config import cargar_configuracion
from modulos.sedes.acceso_datos.mysql_factory import MySQLSedeDAOFactory
from modulos.sedes.acceso_datos.postgres_factory import PostgresSedeDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresSedeDAOFactory()
    return MySQLSedeDAOFactory()