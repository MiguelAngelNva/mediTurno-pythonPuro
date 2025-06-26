from modulos.estados.acceso_datos.estado_dao import EstadoDAOPostgres
from modulos.estados.acceso_datos.dao_factory import EstadoDAOFactory

class PostgresEstadoDAOFactory(EstadoDAOFactory):
    def crear_dao(self):
        return EstadoDAOPostgres