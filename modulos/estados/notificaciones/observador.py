import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    filename="modulos/estados/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, estado):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, estado):
        mensaje = f"[Usuario] Se notificó sobre un nuevo estado: {estado.est_nombre} de la entidad {estado.est_entidad}."
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, estado):
        mensaje = f"[Admin] Estado creado/actualizado: ID={estado.est_id}, Entidad={estado.est_entidad}, Nombre={estado.est_nombre}"
        print(mensaje)
        logging.info(mensaje)