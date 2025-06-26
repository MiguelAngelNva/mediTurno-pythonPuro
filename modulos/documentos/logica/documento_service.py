from fastapi import APIRouter, Request, HTTPException
from modulos.documentos.acceso_datos.get_factory import obtener_fabrica
from modulos.documentos.acceso_datos.documento_dto import DocumentoDTO
from modulos.documentos.notificaciones.sujeto import DocumentoSubject
from modulos.documentos.notificaciones.observador import UsuarioNotificador, AdminNotificador

dao = obtener_fabrica().crear_dao()
router = APIRouter()

sujeto = DocumentoSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())

@router.post("/")
async def crear_documento(req: Request):
    data = await req.json()
    doc = DocumentoDTO(
        doc_tipo_documento=data["doc_tipo_documento"],
        doc_numero_documento=data["doc_numero_documento"],
        doc_fecha_expedicion=data["doc_fecha_expedicion"],
        ciu_id=data["ciu_id"]
    )
    dao.guardar(doc)

    sujeto.notificar(doc)

    return {"mensaje": "Documento creado correctamente."}


@router.get("/")
def obtener_documentos():
    return [d.__dict__ for d in dao.obtener_todos()]


@router.get("/{id}")
def obtener_documento(id: int):
    doc = dao.obtener_por_id(id)
    if not doc:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    return doc.__dict__


@router.put("/{id}")
async def actualizar_documento(id: int, req: Request):
    data = await req.json()
    doc = DocumentoDTO(
        doc_id=id,
        doc_tipo_documento=data["doc_tipo_documento"],
        doc_numero_documento=data["doc_numero_documento"],
        doc_fecha_expedicion=data["doc_fecha_expedicion"],
        ciu_id=data["ciu_id"]
    )
    dao.actualizar(doc)
    sujeto.notificar(doc) 
    return {"mensaje": "Documento actualizado correctamente."}


@router.delete("/{id}")
def eliminar_documento(id: int):
    dao.eliminar(id)
    return {"mensaje": "Documento eliminado correctamente."}