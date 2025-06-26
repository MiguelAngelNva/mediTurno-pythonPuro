from modulos.notificadores.acceso_datos.notificador_dao import NotificadorDAOMySQL
from modulos.notificadores.acceso_datos.dao_factory import NotificadorDAOFactory

class MySQLNotificadorDAOFactory(NotificadorDAOFactory):
    def crear_dao(self):
        return NotificadorDAOMySQL()