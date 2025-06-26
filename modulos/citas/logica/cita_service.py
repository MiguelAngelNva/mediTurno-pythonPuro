from fastapi import APIRouter, Request, HTTPException
from modulos.citas.acceso_datos.get_factory import obtener_fabrica
from modulos.citas.acceso_datos.cita_dto import CitaDTO
from modulos.citas.notificaciones.sujeto import CitaSubject
from modulos.citas.notificaciones.observador import UsuarioNotificador, AdminNotificador

dao = obtener_fabrica().crear_dao()
router = APIRouter()

sujeto = CitaSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())

@router.post("/")
async def crear_cita(req: Request):
    data = await req.json()
    cita = CitaDTO(
        cit_fecha=data["cit_fecha"],
        cit_hora=data["cit_hora"],
        tip_cit_id=data["tip_cit_id"],
        med_id=data["med_id"],
        pac_id=data["pac_id"],
        sed_id=data["sed_id"],
        est_id=data["est_id"]
    )
    dao.guardar(cita)
    sujeto.notificar(cita)
    return {"mensaje": "Cita creada correctamente."}

@router.get("/")
def obtener_citas():
    return [c.__dict__ for c in dao.obtener_todos()]

@router.get("/{id}")
def obtener_cita(id: int):
    cita = dao.obtener_por_id(id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita.__dict__

@router.put("/{id}")
async def actualizar_cita(id: int, req: Request):
    data = await req.json()
    cita = CitaDTO(
        cit_id=id,
        cit_fecha=data["cit_fecha"],
        cit_hora=data["cit_hora"],
        tip_cit_id=data["tip_cit_id"],
        med_id=data["med_id"],
        pac_id=data["pac_id"],
        sed_id=data["sed_id"],
        est_id=data["est_id"]
    )
    dao.actualizar(cita)
    sujeto.notificar(cita)
    return {"mensaje": "Cita actualizada correctamente."}

@router.delete("/{id}")
def eliminar_cita(id: int):
    dao.eliminar(id)
    return {"mensaje": "Cita eliminada correctamente."}