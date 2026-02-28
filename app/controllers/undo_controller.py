from fastapi import APIRouter, status
from pydantic import BaseModel
from app.services import undo_service

router = APIRouter(prefix="/deshacer", tags=["Historial (Pila - LIFO)"])

class Accion(BaseModel):
    descripcion: str

@router.post("/registrar", status_code=status.HTTP_201_CREATED, summary="Guardar acción")
def registrar_accion(accion: Accion):
    return undo_service.push_action(accion.descripcion)

@router.post("/ejecutar", status_code=status.HTTP_200_OK, summary="Deshacer última acción")
def ejecutar_deshacer():
    return undo_service.pop_action()

@router.get("/", status_code=status.HTTP_200_OK, summary="Ver historial")
def ver_historial():
    return undo_service.get_history()