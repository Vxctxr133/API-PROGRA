# 🚀 Proyecto: TaskFlow API - Gestión de Tareas

**Desarrollado para:** [Nombre del Curso o Materia]  
**Estudiante:** [Tu Nombre Completo]  
**Carné / Matrícula:** [Tu Número de Carné]  
**Catedrático:** [Nombre del Ingeniero]  

---

## 🎯 Objetivo del Proyecto
Este repositorio contiene la implementación de una API RESTful desarrollada con **FastAPI**. El propósito estricto de este proyecto es demostrar la capacidad de construir e implementar **Estructuras de Datos Lineales desde cero** (utilizando Nodos en memoria) para la gestión temporal de datos, aplicando **Arquitectura por Capas**.

---

## 📋 Cumplimiento de la Rúbrica de Evaluación

Para facilitar la revisión, a continuación se detalla cómo el proyecto cumple con los requisitos solicitados:

- ✅ **API Funcional:** La API levanta sin errores mediante Uvicorn y responde a todos los endpoints solicitados.
- ✅ **Estructuras de Datos (En memoria):** No se utilizaron listas nativas de Python para el almacenamiento. Se implementaron Nodos manualmente para:
  - **Lista Enlazada:** Gestión del *Backlog* de tareas.
  - **Cola (FIFO):** Gestión de ejecución y procesamiento de tareas.
  - **Pila (LIFO):** Gestión del historial para la función "Deshacer".
- ✅ **Arquitectura por Capas:** Separación estricta en `Controllers` (rutas), `Services` (lógica de negocio y validaciones) y `Repositories` (estructuras de datos puras).
- ✅ **Status Codes y Manejo de Errores:** Se implementaron validaciones lógicas devolviendo códigos `200/201` para éxito, `400 Bad Request` (ej. datos vacíos) y `404 Not Found` (ej. intentar procesar una cola vacía).
- ✅ **Documentación:** Instrucciones de ejecución, explicación de arquitectura y comandos cURL de prueba incluidos en este README.

---

## 💻 Instrucciones para Levantar el Proyecto

Para evaluar la API en un entorno local, ejecute los siguientes comandos en la terminal:

**1. Clonar el repositorio y acceder a la carpeta:**
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd API-PROGRA
```

**2. Crear y activar el entorno virtual:**
```bash
python3 -m venv venv
source venv/bin/activate  # En macOS/Linux
# En Windows usar: venv\Scripts\activate
```

**3. Instalar dependencias requeridas:**
```bash
pip install fastapi uvicorn pydantic
```

**4. Iniciar el servidor de desarrollo:**
```bash
uvicorn main:app --reload
```

🌐 Una vez ejecutado, la interfaz gráfica interactiva (Swagger UI) estará disponible en:
👉 **http://127.0.0.1:8000/docs**

---

## 📡 Ejemplos de Uso (Comandos cURL)

A continuación, se proporcionan los comandos directos para probar el correcto funcionamiento de las tres estructuras de datos.

### 📝 1. Backlog (Lista Enlazada)

**Agregar una nueva tarea al backlog:**
```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/tareas/](http://127.0.0.1:8000/tareas/)' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Diseñar Base de Datos",
  "description": "Crear el diagrama Entidad-Relación",
  "priority": 1
}'
```

**Ver todas las tareas registradas:**
```bash
curl -X 'GET' '[http://127.0.0.1:8000/tareas/](http://127.0.0.1:8000/tareas/)'
```

### 🚶‍♂️ 2. Ejecución (Cola - FIFO)

**Mandar una tarea a la cola de proceso:**
```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/cola/](http://127.0.0.1:8000/cola/)' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Revisar logs de servidor",
  "description": "Buscar errores 500",
  "priority": 2
}'
```

**Procesar tarea (Atiende a la primera que entró en la cola):**
```bash
curl -X 'GET' '[http://127.0.0.1:8000/cola/procesar](http://127.0.0.1:8000/cola/procesar)'
```

### 📚 3. Historial (Pila - LIFO)

**Registrar una acción en el historial:**
```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/deshacer/registrar](http://127.0.0.1:8000/deshacer/registrar)' \
  -H 'Content-Type: application/json' \
  -d '{
  "descripcion": "El usuario borró el archivo index.html"
}'
```

**Deshacer acción (Extrae la última acción registrada en la pila):**
```bash
curl -X 'POST' '[http://127.0.0.1:8000/deshacer/ejecutar](http://127.0.0.1:8000/deshacer/ejecutar)'
```