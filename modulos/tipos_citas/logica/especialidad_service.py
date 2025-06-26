import json
from fastapi import APIRouter, Request, HTTPException
from modulos.tipos_citas.acceso_datos.get_factory import obtener_fabrica
from modulos.tipos_citas.acceso_datos.tipos_citas_dto import Tipos_citasDTO
from modulos.tipos_citas.notificaciones.sujeto import Tipo_citaSubject
from modulos.tipos_citas.notificaciones.observador import UsuarioNotificador, AdminNotificador

dao = obtener_fabrica().crear_dao()
sujeto = Tipo_citaSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())

router = APIRouter()

@router.post("/")
async def crear_tipo_cita(req: Request):
    data = await req.json()
    tipo_cita = Tipos_citasDTO(
        tip_cit_id=data["tip_cit_id"],
        tip_cit_nombre=data["tip_cit_nombre"]
    )
    dao.guardar(tipo_cita)

    if not tipo_cita.tip_cit_id or tipo_cita.tip_cit_id.strip() == "":
        sujeto.notificar(tipo_cita)

    return {"mensaje": "Tipo almacenado correctamente."}


@router.get("/")
def obtener_tipos_citas():
    return [m.__dict__ for m in dao.obtener_todos()]


@router.get("/{id}")
def obtener_tipo_cita(id: int):
    tipo_cita = dao.obtener_por_id(id)
    if not tipo_cita:
        raise HTTPException(status_code=404, detail="Tipo no encontrado")
    return tipo_cita.__dict__


@router.put("/{id}")
async def actualizar_tipo_cita(id: int, req: Request):
    data = await req.json()
    tipo_cita = Tipos_citasDTO(
        tip_cit_id=id,
        tip_cit_id=data["tip_cit_id"]
    )
    dao.actualizar(tipo_cita)
    return {"mensaje": "Tipo actualizado correctamente"}


@router.delete("/{id}")
def eliminar_tipo_cita(id: int):
    dao.eliminar(id)
    return {"mensaje": "Tipo eliminado correctamente."}