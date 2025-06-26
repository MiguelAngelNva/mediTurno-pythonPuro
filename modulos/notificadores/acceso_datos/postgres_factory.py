from modulos.notificadores.acceso_datos.notificador_dao import NotificadorDAOPostgres
from modulos.notificadores.acceso_datos.dao_factory import NotificadorDAOFactory

class PostgresNotificadorDAOFactory(NotificadorDAOFactory):
    def crear_dao(self):
        return NotificadorDAOPostgres