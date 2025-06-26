from modulos.documentos.acceso_datos.documento_dto import DocumentoDTO
from modulos.documentos.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class DocumentoDAOMySQL:
    def guardar(self, doc):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO documentos (doc_tipo_documento, doc_numero_documento, doc_fecha_expedicion, ciu_id)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (doc.doc_tipo_documento, doc.doc_numero_documento, doc.doc_fecha_expedicion, doc.ciu_id))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM documentos")
            rows = cursor.fetchall()
        return [DocumentoDTO(*row) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM documentos WHERE doc_id = %s", (id,))
            row = cursor.fetchone()
        return DocumentoDTO(*row) if row else None

    def actualizar(self, doc):
        with conn.cursor() as cursor:
            sql = """
                UPDATE documentos SET doc_tipo_documento=%s, doc_numero_documento=%s,
                doc_fecha_expedicion=%s, ciu_id=%s WHERE doc_id=%s
            """
            cursor.execute(sql, (doc.doc_tipo_documento, doc.doc_numero_documento, doc.doc_fecha_expedicion, doc.ciu_id, doc.doc_id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM documentos WHERE doc_id = %s", (id,))
        conn.commit()


class DocumentoDAOPostgres:
    def guardar(self, doc):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO documentos (doc_tipo_documento, doc_numero_documento, doc_fecha_expedicion, ciu_id)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (doc.doc_tipo_documento, doc.doc_numero_documento, doc.doc_fecha_expedicion, doc.ciu_id))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM documentos")
            rows = cursor.fetchall()
        return [DocumentoDTO(*row) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM documentos WHERE doc_id = %s", (id,))
            row = cursor.fetchone()
        return DocumentoDTO(*row) if row else None

    def actualizar(self, doc):
        with conn.cursor() as cursor:
            sql = """
                UPDATE documentos SET doc_tipo_documento=%s, doc_numero_documento=%s,
                doc_fecha_expedicion=%s, ciu_id=%s WHERE doc_id=%s
            """
            cursor.execute(sql, (doc.doc_tipo_documento, doc.doc_numero_documento, doc.doc_fecha_expedicion, doc.ciu_id, doc.doc_id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM documentos WHERE doc_id = %s", (id,))
        conn.commit()