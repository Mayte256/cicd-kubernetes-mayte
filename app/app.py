from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML con CSS integrado - Diseño moderno y atractivo
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Kubernetes - Mayte</title>
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
            max-width: 800px;
            width: 100%;
            animation: fadeIn 0.8s ease-in;
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .logo {
            font-size: 60px;
            margin-bottom: 20px;
        }
        
        h1 {
            color: #333;
            font-size: 2.5em;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .subtitle {
            color: #666;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        
        .info-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            margin: 20px 0;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }
        
        .info-card h2 {
            font-size: 1.8em;
            margin-bottom: 15px;
        }
        
        .info-card p {
            font-size: 1.1em;
            line-height: 1.6;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .feature {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .feature:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }
        
        .feature-icon {
            font-size: 40px;
            margin-bottom: 15px;
        }
        
        .feature h3 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .feature p {
            color: #666;
            font-size: 0.9em;
        }
        
        .tech-stack {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
            margin: 30px 0;
        }
        
        .tech-badge {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 30px;
            border-top: 2px solid #eee;
            color: #666;
        }
        
        .pulse {
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo pulse">🚀</div>
            <h1>CI/CD con Kubernetes</h1>
            <p class="subtitle">Proyecto por Mayte - DevOps Pipeline</p>
        </div>
        
        <div class="info-card">
            <h2>✨ ¡Aplicación Desplegada Exitosamente!</h2>
            <p>Esta aplicación demuestra un pipeline completo de CI/CD utilizando GitHub Actions, 
            Docker y Kubernetes para despliegue automatizado en Render.</p>
        </div>
        
        <div class="features">
            <div class="feature">
                <div class="feature-icon">🔄</div>
                <h3>CI/CD</h3>
                <p>Integración y despliegue continuo automatizado</p>
            </div>
            <div class="feature">
                <div class="feature-icon">🐳</div>
                <h3>Docker</h3>
                <p>Contenedores para portabilidad</p>
            </div>
            <div class="feature">
                <div class="feature-icon">☸️</div>
                <h3>Kubernetes</h3>
                <p>Orquestación de contenedores</p>
            </div>
            <div class="feature">
                <div class="feature-icon">⚡</div>
                <h3>GitHub Actions</h3>
                <p>Automatización del pipeline</p>
            </div>
        </div>
        
        <h2 style="text-align: center; color: #333; margin: 30px 0;">🛠️ Tecnologías Utilizadas</h2>
        <div class="tech-stack">
            <span class="tech-badge">Python Flask</span>
            <span class="tech-badge">Docker</span>
            <span class="tech-badge">Kubernetes</span>
            <span class="tech-badge">GitHub Actions</span>
            <span class="tech-badge">Render</span>
        </div>
        
        <div class="footer">
            <p><strong>Desarrollado por:</strong> Mayte</p>
            <p><strong>Host:</strong> bryon.com</p>
            <p style="margin-top: 15px; font-size: 0.9em;">
                Pipeline CI/CD - DevOps Project 2025
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
    return {'status': 'healthy', 'app': 'CI/CD Kubernetes - Mayte'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)