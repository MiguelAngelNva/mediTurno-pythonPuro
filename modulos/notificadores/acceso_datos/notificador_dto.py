from datetime import datetime

class NotificadorDTO:
    def __init__(self, not_id=None, not_tipo="", not_fecha_envio=None, cit_id=None):
        self.not_id = not_id
        self.not_tipo = not_tipo
        self.not_fecha_envio = not_fecha_envio or datetime.now()
        self.cit_id = cit_id

    def __str__(self):
        return f"NotificadorDTO({self.__dict__})"