# MisNotas 📝

Esta es una aplicación web para gestionar notas personales, construida con Flask. Permite crear, editar, eliminar y buscar notas con soporte para etiquetas.

## ¿Qué hace?

- **Crear notas**: título, contenido y una o varias etiquetas
- **Editar notas**: modifica cualquier nota existente
- **Eliminar notas**: con confirmación antes de borrar
- **Buscar**: filtra notas por texto en tiempo real
- **Filtrar por etiqueta**: muestra solo las notas de una categoría

## Tecnologías

- Python 3
- Flask 3.0.3

## Instalación y uso

1. Clona o descarga el proyecto
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:

```bash
python app.py
```

4. Abre tu navegador en `http://127.0.0.1:5000`

## Estructura del proyecto

```
notas-app/
├── app.py              # Lógica principal y rutas de Flask
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Este archivo
└── templates/
    ├── index.html      # Página principal (lista y formulario)
    └── editar.html     # Página de edición de nota
```

## Notas sobre el almacenamiento

Las notas se guardan en memoria mientras la aplicación esté corriendo. Al reiniciar el servidor, los datos se pierden. Para persistencia real se podría integrar una base de datos.

## Autoría

Desarrollado por Daniel Alejandro Cangrejo López para la prueba de Python Pro
