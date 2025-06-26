import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    filename="modulos/medico_especialidad/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, relacion):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, relacion):
        mensaje = f"[Usuario] Se notificó sobre la asignación de especialidad (esp_id={relacion.esp_id}) al médico (med_id={relacion.med_id})"
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, relacion):
        mensaje = f"[Admin] Atención: Se detectó una asignación manual o vacía de especialidad para med_id={relacion.med_id}, esp_id={relacion.esp_id}"
        print(mensaje)
        logging.info(mensaje)
