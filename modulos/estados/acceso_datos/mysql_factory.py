from modulos.estados.acceso_datos.estado_dao import EstadoDAOMySQL
from modulos.estados.acceso_datos.dao_factory import EstadoDAOFactory

class MySQLEstadoDAOFactory(EstadoDAOFactory):
    def crear_dao(self):
        return EstadoDAOMySQL()