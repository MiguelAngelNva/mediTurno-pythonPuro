from modulos.sedes.acceso_datos.sede_dto import SedeDTO
from modulos.sedes.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class SedeDAOMySQL:
    def guardar(self, sede):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO sedes (
                    sed_nombre, sed_tipo_via, sed_numero_via, sed_numero_complemento,
                    sed_barrio, sed_departamento, sed_codigo_postal,
                    sed_detalles_direccion, ciu_id, est_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                sede.sed_nombre, sede.sed_tipo_via, sede.sed_numero_via,
                sede.sed_numero_complemento, sede.sed_barrio, sede.sed_departamento,
                sede.sed_codigo_postal, sede.sed_detalles_direccion, sede.ciu_id, sede.est_id
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sedes")
            rows = cursor.fetchall()
        return [SedeDTO(*row) for row in rows]

    def obtener_por_id(self, sed_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sedes WHERE sed_id = %s", (sed_id,))
            row = cursor.fetchone()
        return SedeDTO(*row) if row else None

    def actualizar(self, sede):
        with conn.cursor() as cursor:
            sql = """
                UPDATE sedes SET sed_nombre=%s, sed_tipo_via=%s, sed_numero_via=%s,
                sed_numero_complemento=%s, sed_barrio=%s, sed_departamento=%s,
                sed_codigo_postal=%s, sed_detalles_direccion=%s, ciu_id=%s, est_id=%s
                WHERE sed_id=%s
            """
            cursor.execute(sql, (
                sede.sed_nombre, sede.sed_tipo_via, sede.sed_numero_via,
                sede.sed_numero_complemento, sede.sed_barrio, sede.sed_departamento,
                sede.sed_codigo_postal, sede.sed_detalles_direccion,
                sede.ciu_id, sede.est_id, sede.sed_id
            ))
        conn.commit()

    def eliminar(self, sed_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM sedes WHERE sed_id = %s", (sed_id,))
        conn.commit()

class SedeDAOPostgres(SedeDAOMySQL):
    def guardar(self, sede):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO sedes (
                    sed_nombre, sed_tipo_via, sed_numero_via, sed_numero_complemento,
                    sed_barrio, sed_departamento, sed_codigo_postal,
                    sed_detalles_direccion, ciu_id, est_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                sede.sed_nombre, sede.sed_tipo_via, sede.sed_numero_via,
                sede.sed_numero_complemento, sede.sed_barrio, sede.sed_departamento,
                sede.sed_codigo_postal, sede.sed_detalles_direccion, sede.ciu_id, sede.est_id
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sedes")
            rows = cursor.fetchall()
        return [SedeDTO(*row) for row in rows]

    def obtener_por_id(self, sed_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM sedes WHERE sed_id = %s", (sed_id,))
            row = cursor.fetchone()
        return SedeDTO(*row) if row else None

    def actualizar(self, sede):
        with conn.cursor() as cursor:
            sql = """
                UPDATE sedes SET sed_nombre=%s, sed_tipo_via=%s, sed_numero_via=%s,
                sed_numero_complemento=%s, sed_barrio=%s, sed_departamento=%s,
                sed_codigo_postal=%s, sed_detalles_direccion=%s, ciu_id=%s, est_id=%s
                WHERE sed_id=%s
            """
            cursor.execute(sql, (
                sede.sed_nombre, sede.sed_tipo_via, sede.sed_numero_via,
                sede.sed_numero_complemento, sede.sed_barrio, sede.sed_departamento,
                sede.sed_codigo_postal, sede.sed_detalles_direccion,
                sede.ciu_id, sede.est_id, sede.sed_id
            ))
        conn.commit()

    def eliminar(self, sed_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM sedes WHERE sed_id = %s", (sed_id,))
        conn.commit()