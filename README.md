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


