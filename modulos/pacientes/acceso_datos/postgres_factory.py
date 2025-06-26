from modulos.pacientes.acceso_datos.paciente_dao import PacienteDAOPostgres
from modulos.pacientes.acceso_datos.dao_factory import PacienteDAOFactory

class PostgresPacienteDAOFactory(PacienteDAOFactory):
    def crear_dao(self):
        return PacienteDAOPostgres