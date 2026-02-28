from fastapi import HTTPException, status
from app.repositories.undo_repo import undo_database

def push_action(descripcion: str):
    if not descripcion.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="La descripción de la acción no puede estar vacía."
        )
    return undo_database.push(descripcion)

def pop_action():
    if undo_database.top is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="La pila de historial está vacía, no hay nada que deshacer."
        )
    return undo_database.pop()

def get_history():
    history = undo_database.ver_pila()
    if not history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="El historial está vacío."
        )
    return history