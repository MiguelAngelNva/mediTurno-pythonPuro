class SedeDTO:
    def __init__(self, sed_id=None, sed_nombre="", sed_tipo_via="", sed_numero_via="",
                 sed_numero_complemento="", sed_barrio="", sed_departamento="",
                 sed_codigo_postal="", sed_detalles_direccion="", ciu_id=None, est_id=None):
        self.sed_id = sed_id
        self.sed_nombre = sed_nombre
        self.sed_tipo_via = sed_tipo_via
        self.sed_numero_via = sed_numero_via
        self.sed_numero_complemento = sed_numero_complemento
        self.sed_barrio = sed_barrio
        self.sed_departamento = sed_departamento
        self.sed_codigo_postal = sed_codigo_postal
        self.sed_detalles_direccion = sed_detalles_direccion
        self.ciu_id = ciu_id
        self.est_id = est_id

    def __str__(self):
        return f"SedeDTO({self.__dict__})"