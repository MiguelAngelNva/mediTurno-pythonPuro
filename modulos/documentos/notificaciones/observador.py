import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    filename="modulos/documentos/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, documento):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, documento):
        mensaje = (
            f"[Usuario] Se notificó sobre el documento número '{documento.doc_numero_documento}' "
            f"del tipo '{documento.doc_tipo_documento}'."
        )
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, documento):
        mensaje = (
            f"[Admin] Documento registrado: ID={documento.doc_id}, Tipo={documento.doc_tipo_documento}, "
            f"Número={documento.doc_numero_documento}, Ciudad ID={documento.ciu_id}"
        )
        print(mensaje)
        logging.info(mensaje)