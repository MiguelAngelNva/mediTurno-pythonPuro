from modulos.documentos.acceso_datos.documento_dao import DocumentoDAOPostgres
from modulos.documentos.acceso_datos.dao_factory import DocumentoDAOFactory

class PostgresDocumentoDAOFactory(DocumentoDAOFactory):
    def crear_dao(self):
        return DocumentoDAOPostgres