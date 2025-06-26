import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    filename="modulos/medicos/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, medico):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, medico):
        mensaje = f"[Usuario] Nuevo médico registrado: {medico.med_primer_nombre} {medico.med_primer_apellido} ({medico.med_correo})"
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, medico):
        mensaje = f"[Admin] Alta de médico con licencia {medico.med_licencia} y correo {medico.med_correo}"
        print(mensaje)
        logging.info(mensaje)