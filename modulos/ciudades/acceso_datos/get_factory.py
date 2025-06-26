from modulos.ciudades.configuracion.config import cargar_configuracion
from modulos.ciudades.acceso_datos.mysql_factory import MySQLCiudadDAOFactory
from modulos.ciudades.acceso_datos.postgres_factory import PostgresCiudadDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresCiudadDAOFactory()
    return MySQLCiudadDAOFactory()