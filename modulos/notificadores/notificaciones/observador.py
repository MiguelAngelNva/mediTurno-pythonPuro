import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    filename="modulos/notificadores/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, notificador):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, notificador):
        mensaje = f"[Usuario] Se envió notificación tipo '{notificador.not_tipo}' para la cita {notificador.cit_id}"
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, notificador):
        mensaje = f"[Admin] Registro de notificación: tipo={notificador.not_tipo}, cita_id={notificador.cit_id}"
        print(mensaje)
        logging.info(mensaje)