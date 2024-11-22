# Proyecto Django con Bootstrap 5

Este proyecto proporciona una guía paso a paso para crear una aplicación Django utilizando **Bootstrap 5** para el diseño de interfaces.

---

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Pasos del Proyecto](#pasos-del-proyecto)
  - [Configuración del Proyecto](#configuración-del-proyecto)
  - [Creación de Vistas y Modelos](#creación-de-vistas-y-modelos)
  - [Integración de Bootstrap 5](#integración-de-bootstrap-5)
- [Credenciales Sugeridas](#credenciales-sugeridas)
- [Licencia](#licencia)

---

## Requisitos

- Python 3.9 o superior
- Django 4.0 o superior
- Bootstrap 5

---

## Configuración del Entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv venv


## Activación del Entorno

2. Activar el entorno virtual:
    ### Windows
    ```bash
    venv\Scripts\activate

## Instalar Django y Guardar dependencias

3. Intalación Django
    ```bash
    pip install django

## Guardar las dependencias
4. Instalación dependencias
    ```bash
    pip freeze > requirements.txt

## Pasos del Proyecto
5. Crear el Proyecto
    ```bash
    django-admin startproject leccion2

6. Ingresar al directorio del Proyecto
    ```bash
    cd leccion2

7. Creamos la Aplicación
    ```bash
    python manage.py startapp dia2

8. Generar las migraciones iniciales
     ```bash
    python manage.py migrate

## Configuración del Proyecto

9. Conectar el proyecto con la aplicación: Agregar 'dia2' en la lista INSTALLED_APPS dentro del archivo leccion2/settings.py:
    ```bash
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dia2',
    ]

10. Ejecutar el servidor:
    ```bash
    python manage.py runserver

## Creación de Vista y Modelos
11. Creación de Vistas y Modelos Crear vistas en dia2/views.py, index y productos
    ```bash
    from django.shortcuts import render
    from .models import Producto

    def index(request):
        return render(request, 'index.html')

    def productos(request):
        productos = Producto.objects.all()
        return render(request, 'productos.html', {'productos': productos})

12. Crear la carpeta de plantillas en dia2/templates y agregar el archivo index.html:
    ```bash
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index</title>
    </head>
    <body>
        <h1>Hola Mundo</h1>
    </body>
    </html>

13. Configurar rutas en leccion2/urls.py
    ```bash
    from django.contrib import admin
    from django.urls import path
    from dia2 import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.index, name='home'),
    ]
14. Crear un modelo en dia2/models.py:
    ```bash
     from django.db import models

    class Producto(models.Model):
        nombre = models.CharField(max_length=100)
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        descripcion = models.TextField()

        def __str__(self):
            return self.nombre

15. Aplicar las migraciones
    ```bash
    python manage.py makemigrations
    python manage.py migrate

16. Crear un superusuario
    ```bash
    python manage.py createsuperuser

    
17. Registrar el modelo en dia2/admin.py
    ```bash
    from django.contrib import admin
    from .models import Producto

    admin.site.register(Producto)

18. Ejecutar el servidor y verificar el panel de administración
    ```bash
    python manage.py runserver

    URL: http://127.0.0.1:8000/admin

19. Mejoras y configuración de plantillas Crear un archivo base de plantillas Ubicación: templates/base.html
    ```bash
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>{% block title %}Mi Proyecto{% endblock %}</title>
    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
    </html>

20. Modificar vistas en dia2/views.py
    ```bash
    def index(request):
        return render(request, 'dia2/index.html')

    def productos(request):
        productos = Producto.objects.all()
        return render(request, 'dia2/productos.html', {'productos': productos})

21. Configurar la carpeta de plantillas externas en leccion2/settings.py
    ```bash
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
## Integración de Bootstrap5
22. Integración de Bootstrap 5 Instalar Bootstrap 5
    ```bash
    pip install django django-bootstrap-v5

23. Configurar Bootstrap 5 en leccion2/settings.py
    ```bash
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'dia2',
        'bootstrap5',
    ]

24. Modificar las plantillas para usar Bootstrap leccion2/templates/base.html
    ```bash
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {% load bootstrap5 %}
        {% bootstrap_css %}
        <title>Bootstrap Principal</title>
    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
    </html>

25. Archivo: dia2/templates/dia2/productos.html
    ```bash
    {% extends 'base.html' %}

    {% block title %}Productos{% endblock %}

    {% block content %}
    <div class="container mt-4">
        <h1 class="mb-4">Listado de Productos</h1>
        <div class="table-responsive">
            <table class="table table-striped border rounded-3 overflow-hidden">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Nombre</th>
                        <th scope="col">Precio</th>
                        <th scope="col">Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    {% for producto in productos %}
                    <tr>
                        <th scope="row">{{ forloop.counter }}</th>
                        <td>{{ producto.nombre }}</td>
                        <td>${{ producto.precio }}</td>
                        <td>{{ producto.descripcion }}</td>
                    </tr>
                    {% empty %}
                    <tr>
                        <td colspan="4" class="text-center">No hay productos disponibles</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
    {% endblock %}

26. Activar el Servidor para verificar los resultados
    ```bash
    python manage.py runserver

    ```bash
    Accede a:

    Página de inicio: http://127.0.0.1:8000/
    Panel de administración: http://127.0.0.1:8000/admin