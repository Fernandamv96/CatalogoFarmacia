import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()

# En Vercel no hay un paso de "release" para migrar: se aplican las migraciones
# pendientes al arrancar la función y se crea el superusuario si se definieron
# DJANGO_SUPERUSER_USERNAME / DJANGO_SUPERUSER_PASSWORD (y opcionalmente DJANGO_SUPERUSER_EMAIL).
if os.environ.get("VERCEL") == "1":
    from django.contrib.auth import get_user_model
    from django.core.management import call_command

    call_command("migrate", interactive=False, verbosity=0)

    username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
    if username and password:
        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username, os.environ.get("DJANGO_SUPERUSER_EMAIL", ""), password
            )

app = application
