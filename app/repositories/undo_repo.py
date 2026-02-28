class StackNode:
    def __init__(self, descripcion: str):
        self.descripcion = descripcion
        self.next = None

class UndoRepository:
    def __init__(self):
        self.top = None  # La "cima" de la pila

    # Agregar a la pila (Push)
    def push(self, descripcion: str):
        new_node = StackNode(descripcion)
        new_node.next = self.top
        self.top = new_node
        return {"mensaje": f"Acción registrada: {descripcion}"}

    # Deshacer / Sacar de la pila (Pop)
    def pop(self):
        if self.top is None:
            return {"mensaje": "La pila está vacía, no hay nada que deshacer."}
        
        accion_deshecha = self.top.descripcion
        self.top = self.top.next
        return {"mensaje": f"Se deshizo la acción: {accion_deshecha}"}

    # Ver el historial
    def ver_pila(self):
        historial = []
        current = self.top
        while current:
            historial.append(current.descripcion)
            current = current.next
        return historial

# Base de datos en memoria para la Pila
undo_database = UndoRepository()