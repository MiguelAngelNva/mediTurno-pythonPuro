from modulos.tipos_citas.acceso_datos.tipos_citas_dto import Tipos_citasDTO
from modulos.tipos_citas.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class Tipo_citaDAOMySQL:
    def guardar(self, tipos_citas_dto):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO `tipos_citas` (`tip_cit_id`, `tip_cit_nombre`) VALUES (%s, %s)
            """
            cursor.execute(sql, (
                tipos_citas_dto.tip_cit_id,
                tipos_citas_dto.tip_cit_nombre,
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tipos_citas")
            rows = cursor.fetchall()
        return [Tipos_citasDTO(*row) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tipos_citas WHERE tip_cit_id = %s", (id,))
            row = cursor.fetchone()
        return Tipos_citasDTO(*row) if row else None

    def actualizar(self, tipos_citas_dto):
        with conn.cursor() as cursor:
            sql = """
                UPDATE tipos_citas SET
                    tip_cit_id=%s, tip_cit_nombre=%s
                WHERE tip_cit_id = %s
            """
            cursor.execute(sql, (
                tipos_citas_dto.tip_cit_id,
                tipos_citas_dto.tip_cit_nombre,
            ))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM tipos_citas WHERE tip_cit_id = %s", (id,))
        conn.commit()


class Tipo_citaDAOPostgres:
    def guardar(self, tipos_citas_dto):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO `tipos_citas` (`tip_cit_id`, `tip_cit_nombre`) VALUES (%s, %s)
            """
            cursor.execute(sql, (
                tipos_citas_dto.tip_cit_id,
                tipos_citas_dto.tip_cit_nombre,
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tipos_citas")
            rows = cursor.fetchall()
        return [Tipos_citasDTO(*row) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tipos_citas WHERE tip_cit_id = %s", (id,))
            row = cursor.fetchone()
        return Tipos_citasDTO(*row) if row else None

    def actualizar(self, tipos_citas_dto):
        with conn.cursor() as cursor:
            sql = """
                UPDATE tipos_citas SET
                    tip_cit_id=%s, tip_cit_nombre=%s
                WHERE tip_cit_id = %s
            """
            cursor.execute(sql, (
                tipos_citas_dto.tip_cit_id,
                tipos_citas_dto.tip_cit_nombre,
            ))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM tipos_citas WHERE tip_cit_id = %s", (id,))
        conn.commit()