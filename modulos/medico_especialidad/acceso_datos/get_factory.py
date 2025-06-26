from modulos.medico_especialidad.configuracion.config import cargar_configuracion
from modulos.medico_especialidad.acceso_datos.mysql_factory import MySQLMedicoEspecialidadDAOFactory
from modulos.medico_especialidad.acceso_datos.postgres_factory import PostgresMedicoEspecialidadDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresMedicoEspecialidadDAOFactory()
    return MySQLMedicoEspecialidadDAOFactory()
