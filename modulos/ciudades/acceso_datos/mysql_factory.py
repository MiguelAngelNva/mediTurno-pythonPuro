from modulos.ciudades.acceso_datos.ciudad_dao import CiudadDAOMySQL
from modulos.ciudades.acceso_datos.dao_factory import CiudadDAOFactory

class MySQLCiudadDAOFactory(CiudadDAOFactory):
    def crear_dao(self):
        return CiudadDAOMySQL()