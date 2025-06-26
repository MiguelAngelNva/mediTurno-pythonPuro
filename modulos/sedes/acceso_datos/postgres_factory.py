from modulos.sedes.acceso_datos.sede_dao import SedeDAOPostgres
from modulos.sedes.acceso_datos.dao_factory import SedeDAOFactory

class PostgresSedeDAOFactory(SedeDAOFactory):
    def crear_dao(self):
        return SedeDAOPostgres