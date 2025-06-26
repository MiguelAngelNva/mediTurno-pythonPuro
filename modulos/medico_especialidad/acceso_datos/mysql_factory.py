from modulos.medico_especialidad.acceso_datos.medico_especialidad_dao import MedicoEspecialidadDAOMySQL
from modulos.medico_especialidad.acceso_datos.dao_factory import MedicoEspecialidadDAOFactory

class MySQLMedicoEspecialidadDAOFactory(MedicoEspecialidadDAOFactory):
    def crear_dao(self):
        return MedicoEspecialidadDAOMySQL()
