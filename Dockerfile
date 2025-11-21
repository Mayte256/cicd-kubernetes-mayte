# ===================================
# DOCKERFILE - Receta para crear el contenedor
# ===================================

# PASO 1: Usar imagen base de Python
# Esto es como empezar con un sistema que ya tiene Python instalado
FROM python:3.11-slim

# PASO 2: Establecer el directorio de trabajo
# Todo lo que hagamos será dentro de /app
WORKDIR /app

# PASO 3: Copiar archivo de dependencias
# Lo copiamos primero para aprovechar el cache de Docker
COPY app/requirements.txt .

# PASO 4: Instalar las dependencias de Python
# pip es el gestor de paquetes de Python
RUN pip install --no-cache-dir -r requirements.txt

# PASO 5: Copiar todo el código de la aplicación
COPY app/ .

# PASO 6: Exponer el puerto 5000
# Le decimos a Docker que nuestra app usa este puerto
EXPOSE 5000

# PASO 7: Variable de entorno para Flask
ENV FLASK_APP=app.py
ENV APP_VERSION=v1.0

# PASO 8: Comando para ejecutar la aplicación
# Cuando el contenedor inicie, ejecutará este comando
# gunicorn es más robusto que flask run para producción
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]