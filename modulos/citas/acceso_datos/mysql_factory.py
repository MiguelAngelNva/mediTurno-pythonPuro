from modulos.citas.acceso_datos.cita_dao import CitaDAOMySQL
from modulos.citas.acceso_datos.dao_factory import CitaDAOFactory

class MySQLCitaDAOFactory(CitaDAOFactory):
    def crear_dao(self):
        return CitaDAOMySQL()