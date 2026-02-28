from app.models.task_model import Task

# El Nodo es cada "eslabón" de la cadena
class Node:
    def __init__(self, task: Task):
        self.task = task
        self.next = None

# La Lista Enlazada para almacenar tareas en memoria
class BacklogRepository:
    def __init__(self):
        self.head = None
        self._count = 1

    def add_task(self, task: Task):
        task.id = self._count
        new_node = Node(task)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._count += 1
        return task

    def get_all(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(current.task)
            current = current.next
        return tasks

# Instancia única para que los datos persistan durante la sesión
backlog_database = BacklogRepository()