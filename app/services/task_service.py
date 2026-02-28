from fastapi import HTTPException, status
from app.models.task_model import Task
from app.repositories.backlog_repo import backlog_database

def create_task(task: Task):
    # Validar que el título no venga vacío (Error 400)
    if not task.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El título de la tarea no puede estar vacío."
        )
    return backlog_database.add_task(task)

def get_all_tasks():
    tasks = backlog_database.get_all()
    # Si la lista enlazada está vacía, devolvemos un 404
    if not tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No hay tareas en el Backlog."
        )
    return tasks