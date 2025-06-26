from modulos.ciudades.acceso_datos.ciudad_dao import CiudadDAOPostgres
from modulos.ciudades.acceso_datos.dao_factory import CiudadDAOFactory

class PostgresCiudadDAOFactory(CiudadDAOFactory):
    def crear_dao(self):
        return CiudadDAOPostgres