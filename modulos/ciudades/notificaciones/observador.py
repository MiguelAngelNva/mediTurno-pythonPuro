import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    filename="modulos/ciudades/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, ciudad):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, ciudad):
        mensaje = f"[Usuario] Se notificó sobre una acción con la ciudad '{ciudad.ciu_nombre}'."
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, ciudad):
        mensaje = f"[Admin] Se registró una acción en la ciudad: ID={ciudad.ciu_id}, Nombre='{ciudad.ciu_nombre}'"
        print(mensaje)
        logging.info(mensaje)