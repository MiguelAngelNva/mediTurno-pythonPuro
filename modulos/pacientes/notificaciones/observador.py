import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    filename="modulos/pacientes/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, paciente):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, paciente):
        mensaje = f"[Usuario] Nuevo paciente registrado: {paciente.pac_primer_nombre} {paciente.pac_primer_apellido}."
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, paciente):
        mensaje = (
            f"[Admin] Registro de paciente: ID={paciente.pac_id}, Correo={paciente.pac_correo}, "
            f"Documento ID={paciente.doc_id}, Estado ID={paciente.est_id}"
        )
        print(mensaje)
        logging.info(mensaje)