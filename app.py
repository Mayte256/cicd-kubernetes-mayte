from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Kubernetes - Mayte,Joel,Damian,Alexis</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 50px;
            max-width: 900px;
            width: 100%;
            animation: fadeIn 0.8s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .logo {
            font-size: 80px;
            margin-bottom: 20px;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        
        h1 {
            color: #333;
            font-size: 2.8em;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .subtitle {
            color: #666;
            font-size: 1.3em;
            margin-bottom: 30px;
        }
        
        .info-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 35px;
            border-radius: 15px;
            margin: 25px 0;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }
        
        .info-card h2 {
            font-size: 2em;
            margin-bottom: 15px;
        }
        
        .info-card p {
            font-size: 1.2em;
            line-height: 1.8;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 25px;
            margin: 35px 0;
        }
        
        .feature {
            background: #f8f9fa;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .feature:hover {
            transform: translateY(-15px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }
        
        .feature-icon {
            font-size: 50px;
            margin-bottom: 20px;
        }
        
        .feature h3 {
            color: #667eea;
            margin-bottom: 12px;
            font-size: 1.3em;
        }
        
        .feature p {
            color: #666;
            font-size: 1em;
        }
        
        .tech-stack {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 18px;
            margin: 35px 0;
        }
        
        .tech-badge {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 25px;
            border-radius: 30px;
            font-weight: bold;
            font-size: 1.1em;
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
            transition: all 0.3s ease;
        }
        
        .tech-badge:hover {
            transform: scale(1.1);
            box-shadow: 0 12px 30px rgba(102, 126, 234, 0.5);
        }
        
        .kubernetes-info {
            background: #f0f4ff;
            border-left: 5px solid #667eea;
            padding: 25px;
            margin: 30px 0;
            border-radius: 10px;
        }
        
        .kubernetes-info h3 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.5em;
        }
        
        .kubernetes-info ul {
            list-style: none;
            padding-left: 0;
        }
        
        .kubernetes-info li {
            padding: 8px 0;
            color: #555;
            font-size: 1.1em;
        }
        
        .kubernetes-info li:before {
            content: "✓ ";
            color: #667eea;
            font-weight: bold;
            margin-right: 10px;
        }
        
        .footer {
            text-align: center;
            margin-top: 50px;
            padding-top: 30px;
            border-top: 2px solid #eee;
            color: #666;
        }
        
        .footer p {
            margin: 10px 0;
            font-size: 1.1em;
        }
        
        .footer strong {
            color: #667eea;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">☸️</div>
            <h1>CI/CD con Kubernetes</h1>
            <p class="subtitle">Pipeline Automatizado - Proyecto por Mayte,Joel,Alexis,Damian</p>
        </div>
        
        <div class="info-card">
            <h2>🚀 ¡Desplegado con Kubernetes Prueba!</h2>
            <p>Esta aplicación demuestra un pipeline completo de CI/CD con GitHub Actions, 
            Docker y Kubernetes. El despliegue es totalmente automatizado desde el código 
            fuente hasta producción.</p>
        </div>
        
        <div class="features">
            <div class="feature">
                <div class="feature-icon">🔄</div>
                <h3>CI/CD Pipeline</h3>
                <p>Integración continua con GitHub Actions</p>
            </div>
            <div class="feature">
                <div class="feature-icon">🐳</div>
                <h3>Docker</h3>
                <p>Containerización para portabilidad</p>
            </div>
            <div class="feature">
                <div class="feature-icon">☸️</div>
                <h3>Kubernetes</h3>
                <p>Orquestación de contenedores</p>
            </div>
            <div class="feature">
                <div class="feature-icon">⚡</div>
                <h3>Auto-Deploy</h3>
                <p>Despliegue automático en cada push</p>
            </div>
        </div>
        
        <div class="kubernetes-info">
            <h3>🎯 Características de Kubernetes</h3>
            <ul>
                <li>2 réplicas del pod para alta disponibilidad</li>
                <li>LoadBalancer service para distribución de tráfico</li>
                <li>Health checks (liveness y readiness probes)</li>
                <li>Rolling updates sin downtime</li>
                <li>Auto-escalado de pods según demanda</li>
                <li>Gestión declarativa con YAML</li>
            </ul>
        </div>
        
        <h2 style="text-align: center; color: #333; margin: 40px 0 25px 0; font-size: 2em;">
            🛠️ Stack Tecnológico
        </h2>
        <div class="tech-stack">
            <span class="tech-badge">Python Flask</span>
            <span class="tech-badge">Docker</span>
            <span class="tech-badge">Kubernetes</span>
            <span class="tech-badge">GitHub Actions</span>
            <span class="tech-badge">Minikube</span>
            <span class="tech-badge">kubectl</span>
        </div>
        
        <div class="footer">
            <p><strong>Desarrollado por:</strong> Mayte</p>
            <p><strong>Host:</strong> bryon.com</p>
            <p><strong>Tecnología:</strong> Kubernetes Orchestration</p>
            <p style="margin-top: 20px; font-size: 1em; color: #999;">
                CI/CD DevOps Pipeline Project - 2025
            </p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return {
        'status': 'healthy',
        'app': 'CI/CD Kubernetes - Mayte',
        'version': '1.0',
        'kubernetes': 'enabled'
    }, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)