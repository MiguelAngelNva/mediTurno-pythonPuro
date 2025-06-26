from datetime import date

class DocumentoDTO:
    def __init__(self, doc_id=None, doc_tipo_documento="", doc_numero_documento="", doc_fecha_expedicion=None, ciu_id=None):
        self.doc_id = doc_id
        self.doc_tipo_documento = doc_tipo_documento
        self.doc_numero_documento = doc_numero_documento
        self.doc_fecha_expedicion = doc_fecha_expedicion or date.today()
        self.ciu_id = ciu_id

    def __str__(self):
        return (f"DocumentoDTO(id={self.doc_id}, tipo='{self.doc_tipo_documento}', "
                f"numero='{self.doc_numero_documento}', fecha={self.doc_fecha_expedicion}, ciudad_id={self.ciu_id})")