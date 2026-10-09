# Crear entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Instalar dependencias dentro del entorno
pip install -r requirements.txt

# Recolectar archivos estáticos
python3 manage.py collectstatic --noinput