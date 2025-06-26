class MedicoDTO:
    def __init__(self, med_id=None, med_primer_nombre="", med_segundo_nombre="",
                 med_primer_apellido="", med_segundo_apellido="", med_telefono="",
                 med_correo="", med_licencia="", doc_id=None, est_id=None):
        self.med_id = med_id
        self.med_primer_nombre = med_primer_nombre
        self.med_segundo_nombre = med_segundo_nombre
        self.med_primer_apellido = med_primer_apellido
        self.med_segundo_apellido = med_segundo_apellido
        self.med_telefono = med_telefono
        self.med_correo = med_correo
        self.med_licencia = med_licencia
        self.doc_id = doc_id
        self.est_id = est_id

    def __str__(self):
        return f"MedicoDTO({self.__dict__})"