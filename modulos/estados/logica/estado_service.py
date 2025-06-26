from fastapi import APIRouter, Request, HTTPException
from modulos.estados.acceso_datos.get_factory import obtener_fabrica
from modulos.estados.acceso_datos.estado_dto import EstadoDTO
from modulos.estados.notificaciones.sujeto import EstadoSubject
from modulos.estados.notificaciones.observador import UsuarioNotificador, AdminNotificador

dao = obtener_fabrica().crear_dao()
router = APIRouter()

sujeto = EstadoSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())

@router.post("/")
async def crear_estado(req: Request):
    data = await req.json()
    estado = EstadoDTO(est_entidad=data["est_entidad"], est_nombre=data["est_nombre"])
    dao.guardar(estado)
    sujeto.notificar(estado)
    return {"mensaje": "Estado creado correctamente."}

@router.get("/")
def obtener_estados():
    return [e.__dict__ for e in dao.obtener_todos()]

@router.get("/{id}")
def obtener_estado(id: int):
    estado = dao.obtener_por_id(id)
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return estado.__dict__

@router.put("/{id}")
async def actualizar_estado(id: int, req: Request):
    data = await req.json()
    estado = EstadoDTO(est_id=id, est_entidad=data["est_entidad"], est_nombre=data["est_nombre"])
    dao.actualizar(estado)
    sujeto.notificar(estado)
    return {"mensaje": "Estado actualizado correctamente."}

@router.delete("/{id}")
def eliminar_estado(id: int):
    dao.eliminar(id)
    return {"mensaje": "Estado eliminado correctamente."}