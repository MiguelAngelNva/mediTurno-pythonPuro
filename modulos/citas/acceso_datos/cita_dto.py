class CitaDTO:
    def __init__(self, cit_id=None, cit_fecha=None, cit_hora=None,
                 tip_cit_id=None, med_id=None, pac_id=None,
                 sed_id=None, est_id=None):
        self.cit_id = cit_id
        self.cit_fecha = cit_fecha
        self.cit_hora = cit_hora
        self.tip_cit_id = tip_cit_id
        self.med_id = med_id
        self.pac_id = pac_id
        self.sed_id = sed_id
        self.est_id = est_id

    def __str__(self):
        return f"CitaDTO({self.__dict__})"