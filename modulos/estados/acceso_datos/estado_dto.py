class EstadoDTO:
    def __init__(self, est_id=None, est_entidad="", est_nombre=""):
        self.est_id = est_id
        self.est_entidad = est_entidad
        self.est_nombre = est_nombre

    def __str__(self):
        return f"EstadoDTO(id={self.est_id}, entidad='{self.est_entidad}', nombre='{self.est_nombre}')"