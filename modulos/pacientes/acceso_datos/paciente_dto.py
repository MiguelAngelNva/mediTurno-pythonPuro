class PacienteDTO:
    def __init__(self, pac_id=None, pac_primer_nombre="", pac_segundo_nombre="",
                 pac_primer_apellido="", pac_segundo_apellido="", pac_telefono="",
                 pac_correo="", doc_id=None, est_id=None):
        self.pac_id = pac_id
        self.pac_primer_nombre = pac_primer_nombre
        self.pac_segundo_nombre = pac_segundo_nombre
        self.pac_primer_apellido = pac_primer_apellido
        self.pac_segundo_apellido = pac_segundo_apellido
        self.pac_telefono = pac_telefono
        self.pac_correo = pac_correo
        self.doc_id = doc_id
        self.est_id = est_id

    def __str__(self):
        return f"PacienteDTO({self.__dict__})"