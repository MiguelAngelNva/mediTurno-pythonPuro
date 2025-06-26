from modulos.notificadores.configuracion.config import cargar_configuracion
from modulos.notificadores.acceso_datos.mysql_factory import MySQLNotificadorDAOFactory
from modulos.notificadores.acceso_datos.postgres_factory import PostgresNotificadorDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresNotificadorDAOFactory()
    return MySQLNotificadorDAOFactory()