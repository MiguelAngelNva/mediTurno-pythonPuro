import json
from fastapi import APIRouter, Request, HTTPException
from modulos.medico_especialidad.acceso_datos.get_factory import obtener_fabrica
from modulos.medico_especialidad.acceso_datos.medico_especialidad_dto import MedicoEspecialidadDTO

router = APIRouter()
dao = obtener_fabrica().crear_dao()

@router.post("/")
async def crear_medico_especialidad(req: Request):
    data = await req.json()
    try:
        dto = MedicoEspecialidadDTO(
            med_esp_id=None, 
            med_id=data["med_id"],
            esp_id=data["esp_id"]
        )
        dao.guardar(dto)
        return {"mensaje": "Relación médico-especialidad creada correctamente."}
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Falta el campo requerido: {e}")

@router.get("/")
def obtener_todos():
    return [rel.__dict__ for rel in dao.obtener_todos()]

@router.get("/{id}")
def obtener_por_id(id: int):
    rel = dao.obtener_por_id(id)
    if not rel:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    return rel.__dict__

@router.put("/{id}")
async def actualizar(id: int, req: Request):
    data = await req.json()
    try:
        dto = MedicoEspecialidadDTO(
            med_esp_id=id,
            med_id=data["med_id"],
            esp_id=data["esp_id"]
        )
        dao.actualizar(dto)
        return {"mensaje": "Relación médico-especialidad actualizada correctamente."}
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Falta el campo requerido: {e}")

@router.delete("/{id}")
def eliminar(id: int):
    dao.eliminar(id)
    return {"mensaje": "Relación médico-especialidad eliminada correctamente."}
