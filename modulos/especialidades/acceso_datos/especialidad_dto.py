
class EspecialidadDTO:
    def __init__(self, esp_id=None, esp_nombre=""):
        self.esp_id = esp_id
        self.esp_nombre = esp_nombre

    def __str__(self):
        return f"EspecialidadDTO(id={self.esp_id}, nombre='{self.esp_nombre}"