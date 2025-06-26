from fastapi import APIRouter, Request, HTTPException
from modulos.sedes.acceso_datos.get_factory import obtener_fabrica
from modulos.sedes.acceso_datos.sede_dto import SedeDTO
from modulos.sedes.notificaciones.sujeto import SedeSubject
from modulos.sedes.notificaciones.observador import UsuarioNotificador, AdminNotificador

dao = obtener_fabrica().crear_dao()
router = APIRouter()

sujeto = SedeSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())

@router.post("/")
async def crear_sede(req: Request):
    data = await req.json()
    sede = SedeDTO(
        sed_nombre=data["sed_nombre"],
        sed_tipo_via=data["sed_tipo_via"],
        sed_numero_via=data["sed_numero_via"],
        sed_numero_complemento=data["sed_numero_complemento"],
        sed_barrio=data["sed_barrio"],
        sed_departamento=data["sed_departamento"],
        sed_codigo_postal=data["sed_codigo_postal"],
        sed_detalles_direccion=data["sed_detalles_direccion"],
        ciu_id=data["ciu_id"],
        est_id=data["est_id"]
    )
    dao.guardar(sede)
    sujeto.notificar(sede)
    return {"mensaje": "Sede registrada correctamente."}

@router.get("/")
def obtener_sedes():
    return [s.__dict__ for s in dao.obtener_todos()]

@router.get("/{id}")
def obtener_sede(id: int):
    sede = dao.obtener_por_id(id)
    if not sede:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return sede.__dict__

@router.put("/{id}")
async def actualizar_sede(id: int, req: Request):
    data = await req.json()
    sede = SedeDTO(
        sed_id=id,
        sed_nombre=data["sed_nombre"],
        sed_tipo_via=data["sed_tipo_via"],
        sed_numero_via=data["sed_numero_via"],
        sed_numero_complemento=data["sed_numero_complemento"],
        sed_barrio=data["sed_barrio"],
        sed_departamento=data["sed_departamento"],
        sed_codigo_postal=data["sed_codigo_postal"],
        sed_detalles_direccion=data["sed_detalles_direccion"],
        ciu_id=data["ciu_id"],
        est_id=data["est_id"]
    )
    dao.actualizar(sede)
    sujeto.notificar(sede)
    return {"mensaje": "Sede actualizada correctamente."}

@router.delete("/{id}")
def eliminar_sede(id: int):
    dao.eliminar(id)
    return {"mensaje": "Sede eliminada correctamente."}