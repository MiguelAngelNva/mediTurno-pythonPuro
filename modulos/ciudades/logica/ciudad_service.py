from fastapi import APIRouter, Request, HTTPException
from modulos.ciudades.acceso_datos.get_factory import obtener_fabrica
from modulos.ciudades.acceso_datos.ciudad_dto import CiudadDTO
from modulos.ciudades.notificaciones.sujeto import CiudadSubject
from modulos.ciudades.notificaciones.observador import UsuarioNotificador, AdminNotificador

dao = obtener_fabrica().crear_dao()

sujeto = CiudadSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())

router = APIRouter()

@router.post("/")
async def crear_ciudad(req: Request):
    data = await req.json()
    ciudad = CiudadDTO(ciu_nombre=data["ciu_nombre"])
    dao.guardar(ciudad)

    sujeto.notificar(ciudad)

    return {"mensaje": "Ciudad almacenada correctamente."}


@router.get("/")
def obtener_ciudades():
    return [c.__dict__ for c in dao.obtener_todos()]


@router.get("/{id}")
def obtener_ciudad(id: int):
    ciudad = dao.obtener_por_id(id)
    if not ciudad:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")
    return ciudad.__dict__


@router.put("/{id}")
async def actualizar_ciudad(id: int, req: Request):
    data = await req.json()
    ciudad = CiudadDTO(ciu_id=id, ciu_nombre=data["ciu_nombre"])
    dao.actualizar(ciudad)
    sujeto.notificar(ciudad)
    return {"mensaje": "Ciudad actualizada correctamente."}


@router.delete("/{id}")
def eliminar_ciudad(id: int):
    dao.eliminar(id)
    return {"mensaje": "Ciudad eliminada correctamente."}