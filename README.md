# 📘 CRUD-ASISTENCIA

**Aplicación web para el registro y gestión de asistencias de estudiantes**  
Implementada con **Django REST Framework** en el backend y **React** en el frontend.

---

## 🛠️ Tecnologías utilizadas

- 💻 **Frontend:** React.js  
- ⚙️ **Backend:** Django + Django REST Framework  
- 🐍 **Lenguaje:** Python  
- 🌐 **API REST**  
- 📦 **Base de datos:** SQLite (por defecto de Django)

---

## 📂 Estructura del proyecto

CRUD-ASISTENCIA/
│
├─ backend/                          # Código del servidor (Django + API REST)
│   ├─ asistencia/                   # Configuración principal del proyecto Django
│   │   ├─ __init__.py               # Inicialización del módulo
│   │   ├─ settings.py               # Configuración general del proyecto
│   │   ├─ urls.py                   # Rutas principales del backend
│   │   ├─ wsgi.py                   # Configuración para despliegue (WSGI)
│   │   └─ asgi.py                   # Configuración para despliegue (ASGI)
│   │
│   ├─ estudiantes/                  # App para gestión de estudiantes
│   │   ├─ __init__.py
│   │   ├─ models.py                 # Modelo de datos de estudiantes
│   │   ├─ serializers.py            # Serializadores para la API
│   │   ├─ views.py                  # Lógica de vistas / controladores
│   │   ├─ urls.py                   # Rutas específicas de esta app
│   │   └─ admin.py                  # Registro de modelos en el panel admin
│   │
│   ├─ asistencias/                  # App para registro de asistencias
│   │   ├─ __init__.py
│   │   ├─ models.py                 # Modelo de datos de asistencias
│   │   ├─ serializers.py            # Serializadores para la API
│   │   ├─ views.py                  # Lógica de vistas / controladores
│   │   ├─ urls.py                   # Rutas específicas de esta app
│   │   └─ admin.py                  # Registro de modelos en el panel admin
│   │
│   ├─ manage.py                     # Script para comandos de Django
│   └─ venv/                         # Entorno virtual de Python
│
├─ frontend/                         # Interfaz de usuario (React)
│   ├─ public/                       # Archivos estáticos públicos
│   └─ src/                          # Código fuente del frontend
│       ├─ components/               # Componentes reutilizables
│       │   ├─ EstudianteForm.js         # Formulario para crear/editar estudiantes
│       │   ├─ EstudianteList.js         # Lista de estudiantes
│       │   ├─ RegistrarAsistenciaForm.js# Formulario para registrar asistencia
│       │   ├─ HistorialAsistencia.js    # Ver historial por estudiante
│       │   └─ EditarAsistenciaForm.js   # Editar registros de asistencia
│       ├─ App.js                    # Componente principal de React
│       └─ index.js                  # Punto de entrada de la app
│
└─ README.md                         # Documentación del proyecto


---

## 🎯 Funcionalidades principales

- 📋 CRUD completo de estudiantes
- ✅ Registro de asistencias
- 📆 Historial de asistencias por estudiante
- ✏️ Edición y eliminación de asistencias

---

## 🚀 Instalación y ejecución

### Backend (Django)

cd backend
python -m venv venv
source venv/bin/activate     # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Frontend (React)
cd frontend
npm install axios
npm start

---

## Metodología
Scrum: Historias de usuario, Sprint Backlog, revisión en un sprint único. XP (Extreme Programming): TDD (tests automáticos), integración continua, feedback rápido.
