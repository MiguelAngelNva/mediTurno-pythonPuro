from modulos.pacientes.acceso_datos.paciente_dto import PacienteDTO
from modulos.pacientes.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class PacienteDAOMySQL:
    def guardar(self, paciente):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO pacientes (
                    pac_primer_nombre, pac_segundo_nombre, pac_primer_apellido, pac_segundo_apellido,
                    pac_telefono, pac_correo, doc_id, est_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                paciente.pac_primer_nombre, paciente.pac_segundo_nombre,
                paciente.pac_primer_apellido, paciente.pac_segundo_apellido,
                paciente.pac_telefono, paciente.pac_correo, paciente.doc_id, paciente.est_id
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pacientes")
            rows = cursor.fetchall()
        return [PacienteDTO(*row) for row in rows]

    def obtener_por_id(self, pac_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pacientes WHERE pac_id = %s", (pac_id,))
            row = cursor.fetchone()
        return PacienteDTO(*row) if row else None

    def actualizar(self, paciente):
        with conn.cursor() as cursor:
            sql = """
                UPDATE pacientes SET pac_primer_nombre=%s, pac_segundo_nombre=%s,
                pac_primer_apellido=%s, pac_segundo_apellido=%s,
                pac_telefono=%s, pac_correo=%s, doc_id=%s, est_id=%s
                WHERE pac_id=%s
            """
            cursor.execute(sql, (
                paciente.pac_primer_nombre, paciente.pac_segundo_nombre,
                paciente.pac_primer_apellido, paciente.pac_segundo_apellido,
                paciente.pac_telefono, paciente.pac_correo,
                paciente.doc_id, paciente.est_id, paciente.pac_id
            ))
        conn.commit()

    def eliminar(self, pac_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM pacientes WHERE pac_id = %s", (pac_id,))
        conn.commit()

class PacienteDAOPostgres(PacienteDAOMySQL):
    def guardar(self, paciente):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO pacientes (
                    pac_primer_nombre, pac_segundo_nombre, pac_primer_apellido, pac_segundo_apellido,
                    pac_telefono, pac_correo, doc_id, est_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                paciente.pac_primer_nombre, paciente.pac_segundo_nombre,
                paciente.pac_primer_apellido, paciente.pac_segundo_apellido,
                paciente.pac_telefono, paciente.pac_correo, paciente.doc_id, paciente.est_id
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pacientes")
            rows = cursor.fetchall()
        return [PacienteDTO(*row) for row in rows]

    def obtener_por_id(self, pac_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pacientes WHERE pac_id = %s", (pac_id,))
            row = cursor.fetchone()
        return PacienteDTO(*row) if row else None

    def actualizar(self, paciente):
        with conn.cursor() as cursor:
            sql = """
                UPDATE pacientes SET pac_primer_nombre=%s, pac_segundo_nombre=%s,
                pac_primer_apellido=%s, pac_segundo_apellido=%s,
                pac_telefono=%s, pac_correo=%s, doc_id=%s, est_id=%s
                WHERE pac_id=%s
            """
            cursor.execute(sql, (
                paciente.pac_primer_nombre, paciente.pac_segundo_nombre,
                paciente.pac_primer_apellido, paciente.pac_segundo_apellido,
                paciente.pac_telefono, paciente.pac_correo,
                paciente.doc_id, paciente.est_id, paciente.pac_id
            ))
        conn.commit()

    def eliminar(self, pac_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM pacientes WHERE pac_id = %s", (pac_id,))
        conn.commit()