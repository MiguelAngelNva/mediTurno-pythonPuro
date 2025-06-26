from modulos.medico_especialidad.acceso_datos.medico_especialidad_dao import MedicoEspecialidadDAOPostgres
from modulos.medico_especialidad.acceso_datos.dao_factory import MedicoEspecialidadDAOFactory

class PostgresMedicoEspecialidadDAOFactory(MedicoEspecialidadDAOFactory):
    def crear_dao(self):
        return MedicoEspecialidadDAOPostgres()
