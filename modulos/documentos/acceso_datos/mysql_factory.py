from modulos.documentos.acceso_datos.documento_dao import DocumentoDAOMySQL
from modulos.documentos.acceso_datos.dao_factory import DocumentoDAOFactory

class MySQLDocumentoDAOFactory(DocumentoDAOFactory):
    def crear_dao(self):
        return DocumentoDAOMySQL()