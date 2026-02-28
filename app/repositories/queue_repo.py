from app.models.task_model import Task

class QueueNode:
    def __init__(self, task: Task):
        self.task = task
        self.next = None

class QueueRepository:
    def __init__(self):
        self.front = None  # El primero de la fila
        self.rear = None   # El último de la fila

    # Agregar a la cola (Enqueue)
    def enqueue(self, task: Task):
        new_node = QueueNode(task)
        if self.rear is None:
            self.front = self.rear = new_node
            return task
        
        self.rear.next = new_node
        self.rear = new_node
        return task

    # Atender/Sacar de la cola (Dequeue)
    def dequeue(self):
        if self.front is None:
            return {"mensaje": "La cola está vacía, no hay tareas por procesar."}
        
        temp = self.front
        self.front = temp.next
        
        if self.front is None:
            self.rear = None
            
        return temp.task

    # Ver quiénes están en la fila (solo para visualizar)
    def ver_cola(self):
        tasks = []
        current = self.front
        while current:
            tasks.append(current.task)
            current = current.next
        return tasks

# Base de datos en memoria para la Cola
queue_database = QueueRepository()