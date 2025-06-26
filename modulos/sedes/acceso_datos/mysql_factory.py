from modulos.sedes.acceso_datos.sede_dao import SedeDAOMySQL
from modulos.sedes.acceso_datos.dao_factory import SedeDAOFactory

class MySQLSedeDAOFactory(SedeDAOFactory):
    def crear_dao(self):
        return SedeDAOMySQL()