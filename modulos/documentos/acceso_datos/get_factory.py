from modulos.documentos.configuracion.config import cargar_configuracion
from modulos.documentos.acceso_datos.mysql_factory import MySQLDocumentoDAOFactory
from modulos.documentos.acceso_datos.postgres_factory import PostgresDocumentoDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresDocumentoDAOFactory()
    return MySQLDocumentoDAOFactory()