import json
from fastapi import APIRouter, Request, HTTPException
from modulos.especialidades.acceso_datos.get_factory import obtener_fabrica
from modulos.especialidades.acceso_datos.especialidad_dto import EspecialidadDTO
from modulos.especialidades.notificaciones.sujeto import EspecialidadSubject
from modulos.medicos.notificaciones.observador import UsuarioNotificador, AdminNotificador

dao = obtener_fabrica().crear_dao()
sujeto = EspecialidadSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())

router = APIRouter()

@router.post("/")
async def crear_especialidad(req: Request):
    data = await req.json()
    especialidad = EspecialidadDTO(
        esp_id=data["esp_id"],
        esp_nombre=data["esp_nombre"]
    )
    dao.guardar(especialidad)

    if not especialidad.esp_id or especialidad.esp_id.strip() == "":
        sujeto.notificar(especialidad)

    return {"mensaje": "Médico almacenado correctamente."}


@router.get("/")
def obtener_especialidades():
    return [m.__dict__ for m in dao.obtener_todos()]


@router.get("/{id}")
def obtener_especialidad(id: int):
    especialidad = dao.obtener_por_id(id)
    if not especialidad:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return especialidad.__dict__


@router.put("/{id}")
async def actualizar_especialidad(id: int, req: Request):
    data = await req.json()
    especialidad = EspecialidadDTO(
        esp_id=id,
        esp_id=data["esp_id"]
    )
    dao.actualizar(especialidad)
    return {"mensaje": "Especialidad Actualizada correctamente."}


@router.delete("/{id}")
def eliminar_especialidad(id: int):
    dao.eliminar(id)
    return {"mensaje": "Especialidad eliminada correctamente."}