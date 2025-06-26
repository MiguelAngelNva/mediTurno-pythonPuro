import json
from fastapi import APIRouter, Request, HTTPException
from modulos.medicos.acceso_datos.get_factory import obtener_fabrica
from modulos.medicos.acceso_datos.medico_dto import MedicoDTO
from modulos.medicos.notificaciones.sujeto import MedicoSubject
from modulos.medicos.notificaciones.observador import UsuarioNotificador, AdminNotificador

dao = obtener_fabrica().crear_dao()
sujeto = MedicoSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())

router = APIRouter()

@router.post("/")
async def crear_medico(req: Request):
    data = await req.json()
    medico = MedicoDTO(
        med_primer_nombre=data["med_primer_nombre"],
        med_segundo_nombre=data["med_segundo_nombre"],
        med_primer_apellido=data["med_primer_apellido"],
        med_segundo_apellido=data["med_segundo_apellido"],
        med_telefono=data["med_telefono"],
        med_correo=data["med_correo"],
        med_licencia=data["med_licencia"],
        doc_id=data["doc_id"],
        est_id=data["est_id"]
    )
    dao.guardar(medico)

    if not medico.med_licencia or medico.med_licencia.strip() == "":
        sujeto.notificar(medico)

    return {"mensaje": "Médico almacenado correctamente."}


@router.get("/")
def obtener_medicos():
    return [m.__dict__ for m in dao.obtener_todos()]


@router.get("/{id}")
def obtener_medico(id: int):
    medico = dao.obtener_por_id(id)
    if not medico:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    return medico.__dict__


@router.put("/{id}")
async def actualizar_medico(id: int, req: Request):
    data = await req.json()
    medico = MedicoDTO(
        med_id=id,
        med_primer_nombre=data["med_primer_nombre"],
        med_segundo_nombre=data["med_segundo_nombre"],
        med_primer_apellido=data["med_primer_apellido"],
        med_segundo_apellido=data["med_segundo_apellido"],
        med_telefono=data["med_telefono"],
        med_correo=data["med_correo"],
        med_licencia=data["med_licencia"],
        doc_id=data["doc_id"],
        est_id=data["est_id"]
    )
    dao.actualizar(medico)
    return {"mensaje": "Médico actualizado correctamente."}


@router.delete("/{id}")
def eliminar_medico(id: int):
    dao.eliminar(id)
    return {"mensaje": "Médico eliminado correctamente."}