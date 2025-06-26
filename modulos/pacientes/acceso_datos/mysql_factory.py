from modulos.pacientes.acceso_datos.paciente_dao import PacienteDAOMySQL
from modulos.pacientes.acceso_datos.dao_factory import PacienteDAOFactory

class MySQLPacienteDAOFactory(PacienteDAOFactory):
    def crear_dao(self):
        return PacienteDAOMySQL()