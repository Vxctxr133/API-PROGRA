from fastapi import APIRouter, status
from app.models.task_model import Task
from app.services import task_service

# APIRouter nos permite separar las rutas de main.py
router = APIRouter(prefix="/tareas", tags=["Backlog (Lista Enlazada)"])

@router.post("/", status_code=status.HTTP_201_CREATED, summary="Agregar una nueva tarea")
def crear_tarea(tarea: Task):
    """Guarda una tarea nueva al final de la Lista Enlazada."""
    return task_service.create_task(tarea)

@router.get("/", status_code=status.HTTP_200_OK, summary="Ver el historial de tareas")
def obtener_tareas():
    """Recorre la Lista Enlazada y devuelve todas las tareas guardadas."""
    return task_service.get_all_tasks()