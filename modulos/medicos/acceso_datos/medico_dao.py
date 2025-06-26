from modulos.medicos.acceso_datos.medico_dto import MedicoDTO
from modulos.medicos.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class MedicoDAOMySQL:
    def guardar(self, medico):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO medicos (
                    med_primer_nombre, med_segundo_nombre, med_primer_apellido, med_segundo_apellido,
                    med_telefono, med_correo, med_licencia, doc_id, est_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                medico.med_primer_nombre, medico.med_segundo_nombre, medico.med_primer_apellido,
                medico.med_segundo_apellido, medico.med_telefono, medico.med_correo,
                medico.med_licencia, medico.doc_id, medico.est_id
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM medicos")
            rows = cursor.fetchall()
        return [MedicoDTO(*row) for row in rows]

    def obtener_por_id(self, med_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM medicos WHERE med_id = %s", (med_id,))
            row = cursor.fetchone()
        return MedicoDTO(*row) if row else None

    def actualizar(self, medico):
        with conn.cursor() as cursor:
            sql = """
                UPDATE medicos SET
                med_primer_nombre=%s, med_segundo_nombre=%s, med_primer_apellido=%s, med_segundo_apellido=%s,
                med_telefono=%s, med_correo=%s, med_licencia=%s, doc_id=%s, est_id=%s
                WHERE med_id=%s
            """
            cursor.execute(sql, (
                medico.med_primer_nombre, medico.med_segundo_nombre, medico.med_primer_apellido,
                medico.med_segundo_apellido, medico.med_telefono, medico.med_correo,
                medico.med_licencia, medico.doc_id, medico.est_id, medico.med_id
            ))
        conn.commit()

    def eliminar(self, med_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM medicos WHERE med_id = %s", (med_id,))
        conn.commit()

class MedicoDAOPostgres(MedicoDAOMySQL):
    def guardar(self, medico):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO medicos (
                    med_primer_nombre, med_segundo_nombre, med_primer_apellido, med_segundo_apellido,
                    med_telefono, med_correo, med_licencia, doc_id, est_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                medico.med_primer_nombre, medico.med_segundo_nombre, medico.med_primer_apellido,
                medico.med_segundo_apellido, medico.med_telefono, medico.med_correo,
                medico.med_licencia, medico.doc_id, medico.est_id
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM medicos")
            rows = cursor.fetchall()
        return [MedicoDTO(*row) for row in rows]

    def obtener_por_id(self, med_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM medicos WHERE med_id = %s", (med_id,))
            row = cursor.fetchone()
        return MedicoDTO(*row) if row else None

    def actualizar(self, medico):
        with conn.cursor() as cursor:
            sql = """
                UPDATE medicos SET
                med_primer_nombre=%s, med_segundo_nombre=%s, med_primer_apellido=%s, med_segundo_apellido=%s,
                med_telefono=%s, med_correo=%s, med_licencia=%s, doc_id=%s, est_id=%s
                WHERE med_id=%s
            """
            cursor.execute(sql, (
                medico.med_primer_nombre, medico.med_segundo_nombre, medico.med_primer_apellido,
                medico.med_segundo_apellido, medico.med_telefono, medico.med_correo,
                medico.med_licencia, medico.doc_id, medico.est_id, medico.med_id
            ))
        conn.commit()

    def eliminar(self, med_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM medicos WHERE med_id = %s", (med_id,))
        conn.commit()