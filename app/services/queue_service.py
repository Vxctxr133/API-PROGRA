from fastapi import HTTPException, status
from app.models.task_model import Task
from app.repositories.queue_repo import queue_database

def enqueue_task(task: Task):
    if not task.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="La tarea debe tener un título válido para entrar a la cola."
        )
    return queue_database.enqueue(task)

def process_task():
    # Validamos si la cola está vacía antes de intentar sacar algo
    if queue_database.front is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="La cola está vacía, no hay tareas por procesar."
        )
    return queue_database.dequeue()

def get_queue():
    tasks = queue_database.ver_cola()
    if not tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No hay tareas esperando en la cola."
        )
    return tasks