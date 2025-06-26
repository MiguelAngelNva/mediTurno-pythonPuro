from modulos.medico_especialidad.acceso_datos.medico_especialidad_dto import MedicoEspecialidadDTO
from modulos.medico_especialidad.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class MedicoEspecialidadDAOMySQL:
    def guardar(self, dto):
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO medico_especialidad (med_id, esp_id) VALUES (%s, %s)", (dto.med_id, dto.esp_id))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM medico_especialidad")
            return [MedicoEspecialidadDTO(*row) for row in cursor.fetchall()]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM medico_especialidad WHERE med_esp_id = %s", (id,))
            row = cursor.fetchone()
        return MedicoEspecialidadDTO(*row) if row else None

    def actualizar(self, dto):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE medico_especialidad SET med_id = %s, esp_id = %s WHERE med_esp_id = %s",
                           (dto.med_id, dto.esp_id, dto.med_esp_id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM medico_especialidad WHERE med_esp_id = %s", (id,))
        conn.commit()


class MedicoEspecialidadDAOPostgres:
    def guardar(self, dto):
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO medico_especialidad (med_id, esp_id) VALUES (%s, %s)", (dto.med_id, dto.esp_id))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM medico_especialidad")
            return [MedicoEspecialidadDTO(*row) for row in cursor.fetchall()]

    def obtener_por_id(self, id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM medico_especialidad WHERE med_esp_id = %s", (id,))
            row = cursor.fetchone()
        return MedicoEspecialidadDTO(*row) if row else None

    def actualizar(self, dto):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE medico_especialidad SET med_id = %s, esp_id = %s WHERE med_esp_id = %s",
                           (dto.med_id, dto.esp_id, dto.med_esp_id))
        conn.commit()

    def eliminar(self, id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM medico_especialidad WHERE med_esp_id = %s", (id,))
        conn.commit()
