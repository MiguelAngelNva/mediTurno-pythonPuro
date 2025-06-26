from modulos.notificadores.acceso_datos.notificador_dto import NotificadorDTO
from modulos.notificadores.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class NotificadorDAOMySQL:
    def guardar(self, notificador):
        with conn.cursor() as cursor:
            sql = "INSERT INTO notificadores (not_tipo, not_fecha_envio, cit_id) VALUES (%s, %s, %s)"
            cursor.execute(sql, (notificador.not_tipo, notificador.not_fecha_envio, notificador.cit_id))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM notificadores")
            rows = cursor.fetchall()
        return [NotificadorDTO(*row) for row in rows]

    def obtener_por_id(self, not_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM notificadores WHERE not_id = %s", (not_id,))
            row = cursor.fetchone()
        return NotificadorDTO(*row) if row else None

    def actualizar(self, notificador):
        with conn.cursor() as cursor:
            sql = """
                UPDATE notificadores SET not_tipo = %s, not_fecha_envio = %s, cit_id = %s
                WHERE not_id = %s
            """
            cursor.execute(sql, (notificador.not_tipo, notificador.not_fecha_envio, notificador.cit_id, notificador.not_id))
        conn.commit()

    def eliminar(self, not_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM notificadores WHERE not_id = %s", (not_id,))
        conn.commit()

class NotificadorDAOPostgres(NotificadorDAOMySQL):
    def guardar(self, notificador):
        with conn.cursor() as cursor:
            sql = "INSERT INTO notificadores (not_tipo, not_fecha_envio, cit_id) VALUES (%s, %s, %s)"
            cursor.execute(sql, (notificador.not_tipo, notificador.not_fecha_envio, notificador.cit_id))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM notificadores")
            rows = cursor.fetchall()
        return [NotificadorDTO(*row) for row in rows]

    def obtener_por_id(self, not_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM notificadores WHERE not_id = %s", (not_id,))
            row = cursor.fetchone()
        return NotificadorDTO(*row) if row else None

    def actualizar(self, notificador):
        with conn.cursor() as cursor:
            sql = """
                UPDATE notificadores SET not_tipo = %s, not_fecha_envio = %s, cit_id = %s
                WHERE not_id = %s
            """
            cursor.execute(sql, (notificador.not_tipo, notificador.not_fecha_envio, notificador.cit_id, notificador.not_id))
        conn.commit()

    def eliminar(self, not_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM notificadores WHERE not_id = %s", (not_id,))
        conn.commit()