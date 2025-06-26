from modulos.citas.configuracion.config import cargar_configuracion
from modulos.citas.acceso_datos.mysql_factory import MySQLCitaDAOFactory
from modulos.citas.acceso_datos.postgres_factory import PostgresCitaDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresCitaDAOFactory()
    return MySQLCitaDAOFactory()