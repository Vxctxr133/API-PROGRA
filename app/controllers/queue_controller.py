from fastapi import APIRouter, status
from app.models.task_model import Task
from app.services import queue_service

router = APIRouter(prefix="/cola", tags=["Ejecución (Cola - FIFO)"])

@router.post("/", status_code=status.HTTP_201_CREATED, summary="Mandar tarea a la cola")
def encolar_tarea(tarea: Task):
    return queue_service.enqueue_task(tarea)

@router.get("/procesar", status_code=status.HTTP_200_OK, summary="Procesar la primera tarea")
def procesar_tarea():
    return queue_service.process_task()

@router.get("/", status_code=status.HTTP_200_OK, summary="Ver tareas en fila")
def ver_cola():
    return queue_service.get_queue()