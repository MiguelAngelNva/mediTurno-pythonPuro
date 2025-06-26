from modulos.medicos.acceso_datos.medico_dao import MedicoDAOMySQL
from modulos.medicos.acceso_datos.dao_factory import MedicoDAOFactory

class MySQLMedicoDAOFactory(MedicoDAOFactory):
    def crear_dao(self):
        return MedicoDAOMySQL()