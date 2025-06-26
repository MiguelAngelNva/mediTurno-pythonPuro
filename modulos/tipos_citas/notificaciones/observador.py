import logging
from abc import ABC, abstractmethod

# Configurar logging para guardar notificaciones en archivo
logging.basicConfig(
    filename="modulos/medicos/logs/notificaciones.log",  # Asegúrate de que esta carpeta exista
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, medico):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, medico):
        mensaje = (
            f"[Usuario] Se notificó al médico {medico.med_primer_nombre} {medico.med_primer_apellido} "
            f"({medico.med_correo}) sobre irregularidades en su registro."
        )
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, medico):
        mensaje = (
            f"[Admin] Atención: Registro inusual de médico: {medico.med_primer_nombre} {medico.med_primer_apellido} "
            f"- Licencia: {medico.med_licencia}, Email: {medico.med_correo}"
        )
        print(mensaje)
        logging.info(mensaje)