from modulos.especialidades.acceso_datos.especialidad_dto import EspecialidadDTO
from modulos.especialidades.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class EspecialidadDAOMySQL:
    def guardar(self, especialidad_dto):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO `especialidades` (`esp_id`, `esp_nombre`) VALUES (%s, %s)
            """
            cursor.execute(sql, (
                especialidad_dto.esp_id,
                especialidad_dto.esp_nombre,
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM especialidades")
            rows = cursor.fetchall()
        return [EspecialidadDTO(*row) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM especialidades WHERE med_id = %s", (id,))
            row = cursor.fetchone()
        return EspecialidadDTO(*row) if row else None

    def actualizar(self, especialidad_dto):
        with conn.cursor() as cursor:
            sql = """
                UPDATE especialidades SET
                    esp_id=%s, esp_nombre=%s
                WHERE med_id = %s
            """
            cursor.execute(sql, (
                especialidad_dto.esp_id,
                especialidad_dto.esp_nombre,
            ))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM especialidades WHERE med_id = %s", (id,))
        conn.commit()


class MedicoDAOPostgres:
    def guardar(self, especialidad_dto):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO `especialidades` (`esp_id`, `esp_nombre`) VALUES (%s, %s)
            """
            cursor.execute(sql, (
                especialidad_dto.esp_id,
                especialidad_dto.esp_nombre,
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM especialidades")
            rows = cursor.fetchall()
        return [EspecialidadDTO(*row) for row in rows]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM especialidades WHERE med_id = %s", (id,))
            row = cursor.fetchone()
        return EspecialidadDTO(*row) if row else None

    def actualizar(self, especialidad_dto):
        with conn.cursor() as cursor:
            sql = """
                UPDATE especialidades SET
                    esp_id=%s, esp_nombre=%s
                WHERE med_id = %s
            """
            cursor.execute(sql, (
                especialidad_dto.esp_id,
                especialidad_dto.esp_nombre,
            ))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM especialidades WHERE med_id = %s", (id,))
        conn.commit()