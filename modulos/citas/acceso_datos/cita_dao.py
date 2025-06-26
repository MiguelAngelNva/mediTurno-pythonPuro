from modulos.citas.acceso_datos.cita_dto import CitaDTO
from modulos.citas.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class CitaDAOMySQL:
    def guardar(self, cita):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO citas (
                    cit_fecha, cit_hora, tip_cit_id, med_id, pac_id, sed_id, est_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                cita.cit_fecha, cita.cit_hora, cita.tip_cit_id,
                cita.med_id, cita.pac_id, cita.sed_id, cita.est_id
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM citas")
            rows = cursor.fetchall()
        return [CitaDTO(*row) for row in rows]

    def obtener_por_id(self, cit_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM citas WHERE cit_id = %s", (cit_id,))
            row = cursor.fetchone()
        return CitaDTO(*row) if row else None

    def actualizar(self, cita):
        with conn.cursor() as cursor:
            sql = """
                UPDATE citas SET cit_fecha=%s, cit_hora=%s, tip_cit_id=%s,
                med_id=%s, pac_id=%s, sed_id=%s, est_id=%s
                WHERE cit_id=%s
            """
            cursor.execute(sql, (
                cita.cit_fecha, cita.cit_hora, cita.tip_cit_id,
                cita.med_id, cita.pac_id, cita.sed_id, cita.est_id, cita.cit_id
            ))
        conn.commit()

    def eliminar(self, cit_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM citas WHERE cit_id = %s", (cit_id,))
        conn.commit()

class CitaDAOPostgres(CitaDAOMySQL):
    def guardar(self, cita):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO citas (
                    cit_fecha, cit_hora, tip_cit_id, med_id, pac_id, sed_id, est_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                cita.cit_fecha, cita.cit_hora, cita.tip_cit_id,
                cita.med_id, cita.pac_id, cita.sed_id, cita.est_id
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM citas")
            rows = cursor.fetchall()
        return [CitaDTO(*row) for row in rows]

    def obtener_por_id(self, cit_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM citas WHERE cit_id = %s", (cit_id,))
            row = cursor.fetchone()
        return CitaDTO(*row) if row else None

    def actualizar(self, cita):
        with conn.cursor() as cursor:
            sql = """
                UPDATE citas SET cit_fecha=%s, cit_hora=%s, tip_cit_id=%s,
                med_id=%s, pac_id=%s, sed_id=%s, est_id=%s
                WHERE cit_id=%s
            """
            cursor.execute(sql, (
                cita.cit_fecha, cita.cit_hora, cita.tip_cit_id,
                cita.med_id, cita.pac_id, cita.sed_id, cita.est_id, cita.cit_id
            ))
        conn.commit()

    def eliminar(self, cit_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM citas WHERE cit_id = %s", (cit_id,))
        conn.commit()