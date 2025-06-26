from modulos.ciudades.acceso_datos.ciudad_dto import CiudadDTO
from modulos.ciudades.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class CiudadDAOMySQL:
    def guardar(self, ciudad_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO ciudades (ciu_nombre) VALUES (%s)"
            cursor.execute(sql, (ciudad_dto.ciu_nombre,))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT ciu_id, ciu_nombre FROM ciudades")
            rows = cursor.fetchall()
        return [CiudadDTO(ciu_id=row[0], ciu_nombre=row[1]) for row in rows]

    def obtener_por_id(self, ciu_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT ciu_id, ciu_nombre FROM ciudades WHERE ciu_id = %s", (ciu_id,))
            row = cursor.fetchone()
        return CiudadDTO(ciu_id=row[0], ciu_nombre=row[1]) if row else None

    def actualizar(self, ciudad_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE ciudades SET ciu_nombre = %s WHERE ciu_id = %s"
            cursor.execute(sql, (ciudad_dto.ciu_nombre, ciudad_dto.ciu_id))
        conn.commit()

    def eliminar(self, ciu_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM ciudades WHERE ciu_id = %s", (ciu_id,))
        conn.commit()


class CiudadDAOPostgres:
    def guardar(self, ciudad_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO ciudades (ciu_nombre) VALUES (%s)"
            cursor.execute(sql, (ciudad_dto.ciu_nombre,))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT ciu_id, ciu_nombre FROM ciudades")
            rows = cursor.fetchall()
        return [CiudadDTO(ciu_id=row[0], ciu_nombre=row[1]) for row in rows]

    def obtener_por_id(self, ciu_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT ciu_id, ciu_nombre FROM ciudades WHERE ciu_id = %s", (ciu_id,))
            row = cursor.fetchone()
        return CiudadDTO(ciu_id=row[0], ciu_nombre=row[1]) if row else None

    def actualizar(self, ciudad_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE ciudades SET ciu_nombre = %s WHERE ciu_id = %s"
            cursor.execute(sql, (ciudad_dto.ciu_nombre, ciudad_dto.ciu_id))
        conn.commit()

    def eliminar(self, ciu_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM ciudades WHERE ciu_id = %s", (ciu_id,))
        conn.commit()