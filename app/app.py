from flask import Flask, jsonify
import os
from datetime import datetime

# Crear la aplicación Flask
app = Flask(__name__)

# RUTA PRINCIPAL - Lo que verás en maytebryon.com
@app.route('/')
def home():
    """
    Esta es la página principal de tu app
    Muestra un mensaje de bienvenida bonito
    """
    return jsonify({
        'mensaje': '🌸 ¡Bienvenida! App de Mayte',
        'descripcion': 'CI/CD con Kubernetes - Proyecto DevOps',
        'version': os.getenv('APP_VERSION', 'v1.0'),
        'timestamp': datetime.now().isoformat(),
        'autor': 'Mayte - Estudiante DevOps'
    })

# RUTA DE SALUD - Kubernetes usa esto para verificar que todo está bien
@app.route('/health')
def health():
    """
    Endpoint de salud
    Responde 200 si la app está funcionando correctamente
    """
    return jsonify({
        'status': 'healthy',
        'service': 'mayte-cicd-demo',
        'uptime': 'running'
    }), 200

# RUTA DE INFORMACIÓN
@app.route('/info')
def info():
    """
    Muestra información detallada del proyecto
    """
    return jsonify({
        'proyecto': 'CI/CD con Kubernetes',
        'universidad': 'Tu Universidad',
        'materia': 'DevOps',
        'tecnologias': [
            'Python 3.11',
            'Flask',
            'Docker',
            'Kubernetes',
            'GitHub Actions',
            'Nginx'
        ],
        'estudiante': 'Mayte',
        'cedula': '1754347704',
        'url': 'maytebryon.com'
    })

# RUTA DE PRESENTACIÓN (para mostrar en clase)
@app.route('/presentacion')
def presentacion():
    """
    Información para la presentación del proyecto
    """
    return jsonify({
        'tema': 'CI/CD con Kubernetes',
        'que_es_cicd': 'Integración y Despliegue Continuo automatizado',
        'que_es_kubernetes': 'Orquestador de contenedores que gestiona aplicaciones',
        'componentes': {
            'Pods': 'Unidad mínima que ejecuta contenedores',
            'Deployment': 'Gestiona réplicas y actualizaciones',
            'Service': 'Expone la aplicación y balancea tráfico'
        },
        'flujo': [
            '1. Desarrollador hace commit y push',
            '2. GitHub Actions construye imagen Docker',
            '3. Imagen se sube a Docker Hub',
            '4. Kubernetes despliega automáticamente',
            '5. App disponible sin downtime'
        ]
    })

# Iniciar la aplicación
if __name__ == '__main__':
    # host='0.0.0.0' permite que se pueda acceder desde cualquier IP
    # port=5000 es el puerto estándar de Flask
    app.run(debug=True, host='0.0.0.0', port=5000)