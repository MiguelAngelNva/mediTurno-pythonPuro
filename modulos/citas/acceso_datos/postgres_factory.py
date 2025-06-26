from modulos.citas.acceso_datos.cita_dao import CitaDAOPostgres
from modulos.citas.acceso_datos.dao_factory import CitaDAOFactory

class PostgresCitaDAOFactory(CitaDAOFactory):
    def crear_dao(self):
        return CitaDAOPostgres