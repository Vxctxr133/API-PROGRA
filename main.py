from fastapi import FastAPI
from app.controllers import task_controller, queue_controller, undo_controller

app = FastAPI(
    title="TaskFlow API - Gestión de Tareas",
    description="API con Arquitectura por Capas y Estructuras de Datos en memoria.",
    version="1.0.0"
)

# Conectamos todos los controladores
app.include_router(task_controller.router)
app.include_router(queue_controller.router)
app.include_router(undo_controller.router)

@app.get("/", tags=["Inicio"], summary="Comprobar estado del servidor")
def inicio():
    return {"¡El servidor base está funcionando perfectamente!"}