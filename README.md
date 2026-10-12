# Catálogo Farmacia

Aplicación Django (CRUD) para gestionar el catálogo de productos de una farmacia.

## Estructura

```
CatalogoFarmacia/
├── core/                  # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py            # Punto de entrada en Vercel
│   └── asgi.py
├── farmacia/              # App del catálogo
│   ├── migrations/
│   ├── templates/farmacia/
│   │   ├── catalogo_list.html
│   │   ├── catalogo_form.html
│   │   └── catalogo_confirm_delete.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── base.html          # Plantilla base compartida
├── manage.py
├── requirements.txt
├── vercel.json
└── .python-version
```

## Desarrollo local

```bash
python -m venv venv
venv\Scripts\activate        # Windows  (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py test       # ejecutar pruebas
```

## Despliegue en Vercel

1. Importar el repositorio en Vercel (framework: **Other**). La configuración está en `vercel.json`.
2. Base de datos: en el proyecto de Vercel → **Storage** → crear una base **Neon (Postgres)** y conectarla.
   Esto añade la variable `DATABASE_URL` automáticamente.
   Sin `DATABASE_URL` la app funciona igual, pero con SQLite temporal: los datos se pierden al reiniciarse.
3. Variables de entorno (Settings → Environment Variables):

   | Variable | Valor |
   |---|---|
   | `SECRET_KEY` | una cadena larga y aleatoria |
   | `DJANGO_SUPERUSER_USERNAME` | usuario para `/admin/` |
   | `DJANGO_SUPERUSER_PASSWORD` | contraseña para `/admin/` |
   | `DJANGO_SUPERUSER_EMAIL` | (opcional) |
   | `DEBUG` | (opcional) `True` solo para depurar |

4. Redesplegar. Las migraciones y el superusuario se crean automáticamente al arrancar (`core/wsgi.py`).

Si se usa un dominio propio, añadirlo en `ALLOWED_HOSTS` y `CSRF_TRUSTED_ORIGINS` (separados por comas, con `https://` en el segundo).
