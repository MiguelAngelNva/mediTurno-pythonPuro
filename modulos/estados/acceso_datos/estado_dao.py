from modulos.estados.acceso_datos.estado_dto import EstadoDTO
from modulos.estados.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class EstadoDAOMySQL:
    def guardar(self, estado):
        with conn.cursor() as cursor:
            sql = "INSERT INTO estados (est_entidad, est_nombre) VALUES (%s, %s)"
            cursor.execute(sql, (estado.est_entidad, estado.est_nombre))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT est_id, est_entidad, est_nombre FROM estados")
            rows = cursor.fetchall()
        return [EstadoDTO(est_id=row[0], est_entidad=row[1], est_nombre=row[2]) for row in rows]

    def obtener_por_id(self, est_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT est_id, est_entidad, est_nombre FROM estados WHERE est_id = %s", (est_id,))
            row = cursor.fetchone()
        return EstadoDTO(est_id=row[0], est_entidad=row[1], est_nombre=row[2]) if row else None

    def actualizar(self, estado):
        with conn.cursor() as cursor:
            sql = "UPDATE estados SET est_entidad = %s, est_nombre = %s WHERE est_id = %s"
            cursor.execute(sql, (estado.est_entidad, estado.est_nombre, estado.est_id))
        conn.commit()

    def eliminar(self, est_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM estados WHERE est_id = %s", (est_id,))
        conn.commit()


class EstadoDAOPostgres:
    def guardar(self, estado):
        with conn.cursor() as cursor:
            sql = "INSERT INTO estados (est_entidad, est_nombre) VALUES (%s, %s)"
            cursor.execute(sql, (estado.est_entidad, estado.est_nombre))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT est_id, est_entidad, est_nombre FROM estados")
            rows = cursor.fetchall()
        return [EstadoDTO(est_id=row[0], est_entidad=row[1], est_nombre=row[2]) for row in rows]

    def obtener_por_id(self, est_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT est_id, est_entidad, est_nombre FROM estados WHERE est_id = %s", (est_id,))
            row = cursor.fetchone()
        return EstadoDTO(est_id=row[0], est_entidad=row[1], est_nombre=row[2]) if row else None

    def actualizar(self, estado):
        with conn.cursor() as cursor:
            sql = "UPDATE estados SET est_entidad = %s, est_nombre = %s WHERE est_id = %s"
            cursor.execute(sql, (estado.est_entidad, estado.est_nombre, estado.est_id))
        conn.commit()

    def eliminar(self, est_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM estados WHERE est_id = %s", (est_id,))
        conn.commit()