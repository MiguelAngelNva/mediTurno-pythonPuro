import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    filename="modulos/citas/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, cita):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, cita):
        mensaje = f"[Usuario] Cita registrada para paciente {cita.pac_id} el {cita.cit_fecha} a las {cita.cit_hora}."
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, cita):
        mensaje = f"[Admin] Nueva cita agendada: Medico ID={cita.med_id}, Paciente ID={cita.pac_id}, Sede ID={cita.sed_id}, Estado={cita.est_id}"
        print(mensaje)
        logging.info(mensaje)