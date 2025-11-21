from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'mensaje': '🌸 Bienvenida - Proyecto CI/CD con Kubernetes',
        'estudiante': 'Mayte',
        'cedula': '1754347704',
        'materia': 'DevOps',
        'version': 'v1.0',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'mayte-app'
    }), 200

@app.route('/info')
def info():
    return jsonify({
        'proyecto': 'CI/CD con Kubernetes',
        'tecnologias': ['Python', 'Flask', 'Docker', 'Kubernetes', 'GitHub Actions'],
        'componentes_kubernetes': {
            'Pods': 'Unidad mínima que ejecuta contenedores',
            'Deployment': 'Gestiona réplicas y actualizaciones',
            'Service': 'Expone la aplicación'
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)