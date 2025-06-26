from fastapi import APIRouter, Request, HTTPException
from modulos.pacientes.acceso_datos.get_factory import obtener_fabrica
from modulos.pacientes.acceso_datos.paciente_dto import PacienteDTO
from modulos.pacientes.notificaciones.sujeto import PacienteSubject
from modulos.pacientes.notificaciones.observador import UsuarioNotificador, AdminNotificador

dao = obtener_fabrica().crear_dao()
router = APIRouter()

sujeto = PacienteSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())

@router.post("/")
async def crear_paciente(req: Request):
    data = await req.json()
    paciente = PacienteDTO(
        pac_primer_nombre=data["pac_primer_nombre"],
        pac_segundo_nombre=data["pac_segundo_nombre"],
        pac_primer_apellido=data["pac_primer_apellido"],
        pac_segundo_apellido=data["pac_segundo_apellido"],
        pac_telefono=data["pac_telefono"],
        pac_correo=data["pac_correo"],
        doc_id=data["doc_id"],
        est_id=data["est_id"]
    )
    dao.guardar(paciente)
    sujeto.notificar(paciente)
    return {"mensaje": "Paciente creado correctamente."}

@router.get("/")
def obtener_pacientes():
    return [p.__dict__ for p in dao.obtener_todos()]

@router.get("/{id}")
def obtener_paciente(id: int):
    paciente = dao.obtener_por_id(id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente.__dict__

@router.put("/{id}")
async def actualizar_paciente(id: int, req: Request):
    data = await req.json()
    paciente = PacienteDTO(
        pac_id=id,
        pac_primer_nombre=data["pac_primer_nombre"],
        pac_segundo_nombre=data["pac_segundo_nombre"],
        pac_primer_apellido=data["pac_primer_apellido"],
        pac_segundo_apellido=data["pac_segundo_apellido"],
        pac_telefono=data["pac_telefono"],
        pac_correo=data["pac_correo"],
        doc_id=data["doc_id"],
        est_id=data["est_id"]
    )
    dao.actualizar(paciente)
    sujeto.notificar(paciente)
    return {"mensaje": "Paciente actualizado correctamente."}

@router.delete("/{id}")
def eliminar_paciente(id: int):
    dao.eliminar(id)
    return {"mensaje": "Paciente eliminado correctamente."}