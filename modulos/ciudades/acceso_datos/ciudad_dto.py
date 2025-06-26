class CiudadDTO:
    def __init__(self, ciu_id=None, ciu_nombre=""):
        self.ciu_id = ciu_id
        self.ciu_nombre = ciu_nombre

    def __str__(self):
        return f"CiudadDTO(id={self.ciu_id}, nombre='{self.ciu_nombre}')"