FROM python:3.11-slim

# Actualiza e instala dependencias básicas (opcional si necesitas alguna librería del SO)
RUN apt-get update && apt-get upgrade -y && apt-get clean

WORKDIR /app

# Copia e instala dependencias
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto de la app
COPY . .

# Ejecuta collectstatic para archivos estáticos
RUN python manage.py collectstatic --noinput

# Expone el puerto 8000 para la app
EXPOSE 8000

# Copia el script de arranque y dale permisos
COPY start.sh .
RUN chmod +x start.sh

# Comando para arrancar contenedor: primero migra, luego arranca gunicorn
CMD ["./start.sh"]
