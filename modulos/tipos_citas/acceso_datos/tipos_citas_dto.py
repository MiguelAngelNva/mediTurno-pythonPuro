
class Tipos_citasDTO:
    def __init__(self, tip_cit_id=None, tip_cit_nombre=""):
        self.tip_cit_id = tip_cit_id
        self.tip_cit_nombre = tip_cit_nombre

    def __str__(self):
        return f"Tipos_citasDTO(id={self.tip_cit_id}, nombre='{self.tip_cit_nombre}"