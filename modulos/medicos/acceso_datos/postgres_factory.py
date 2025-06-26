from modulos.medicos.acceso_datos.medico_dao import MedicoDAOPostgres
from modulos.medicos.acceso_datos.dao_factory import MedicoDAOFactory

class PostgresMedicoDAOFactory(MedicoDAOFactory):
    def crear_dao(self):
        return MedicoDAOPostgres