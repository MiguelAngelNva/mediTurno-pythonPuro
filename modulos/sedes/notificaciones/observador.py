import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    filename="modulos/sedes/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, sede):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, sede):
        mensaje = f"[Usuario] Nueva sede registrada: {sede.sed_nombre} en {sede.sed_barrio}, {sede.sed_departamento}."
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, sede):
        mensaje = f"[Admin] Alta de sede: ID={sede.sed_id}, Código Postal={sede.sed_codigo_postal}, Ciudad={sede.ciu_id}"
        print(mensaje)
        logging.info(mensaje)