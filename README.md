# 🚀 CI/CD con Kubernetes - Proyecto Mayte

## 📖 Descripción
Proyecto de CI/CD automatizado que demuestra:
- Integración continua con GitHub Actions
- Containerización con Docker
- Orquestación con Kubernetes
- Despliegue automatizado

## 👩‍💻 Información del Proyecto
- **Estudiante**: Mayte
- **Cédula**: 1754347704
- **Materia**: DevOps / CI-CD
- **URL**: maytebryon.com

## 🛠️ Tecnologías
- Python 3.11 + Flask
- Docker
- Kubernetes
- GitHub Actions
- Nginx
- Git

## 🏗️ Arquitectura
```
Desarrollador → GitHub → GitHub Actions → Docker Hub → Servidor → Kubernetes
     ↓            ↓            ↓              ↓           ↓          ↓
   Código      Push       Build Image    Store Image   Deploy    Run App
```

## 📦 Estructura del Proyecto
```
cicd-kubernetes-mayte/
├── app/
│   ├── app.py              # Aplicación Flask
│   └── requirements.txt    # Dependencias Python
├── k8s/
│   ├── deployment.yaml     # Configuración Deployment
│   └── service.yaml        # Configuración Service
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # Pipeline CI/CD
├── Dockerfile              # Construcción de imagen
└── README.md              # Este archivo
```

## 🚀 Cómo Funciona

### 1. Desarrollo
```bash
# Modificar código
vim app/app.py

# Probar localmente
python app/app.py
```

### 2. CI/CD Automático
```bash
git add .
git commit -m "Nueva funcionalidad"
git push origin main
# ↓ GitHub Actions se activa automáticamente
```

### 3. Pipeline Ejecuta:
- ✅ Construye imagen Docker
- ✅ Sube a Docker Hub
- ✅ Valida configuraciones K8s
- ✅ Lista para desplegar

### 4. Deployment
```bash
# En el servidor
docker pull tuusuario/mayte-app:latest
docker run -d -p 5000:5000 mayte-app
```

## 🌐 Endpoints

- `GET /` - Página principal
- `GET /health` - Estado de salud
- `GET /info` - Información del proyecto
- `GET /presentacion` - Datos para la exposición

## 📊 Conceptos Clave

### ¿Qué es CI/CD?
**Continuous Integration / Continuous Deployment**
- Automatiza la integración de código
- Despliega automáticamente cada cambio aprobado

### ¿Qué es Kubernetes?
**Orquestador de contenedores**
- Gestiona múltiples copias de la aplicación
- Auto-recuperación ante fallos
- Escalado automático
- Actualizaciones sin downtime

### Componentes de Kubernetes:
- **Pod**: Unidad mínima que ejecuta contenedores
- **Deployment**: Gestiona réplicas y actualizaciones
- **Service**: Expone la aplicación y balancea tráfico

## ✨ Ventajas de este Approach

1. **Automatización**: De código a producción automáticamente
2. **Confiabilidad**: Tests y validaciones automáticas
3. **Escalabilidad**: Fácil aumentar/disminuir recursos
4. **Resiliencia**: Auto-recuperación ante fallos
5. **Velocidad**: Deployments en minutos

## 🎓 Para la Exposición

### Puntos Clave:
1. **CI/CD automatiza** todo el ciclo de desarrollo
2. **Docker empaqueta** la aplicación de forma portable
3. **Kubernetes gestiona** múltiples instancias automáticamente
4. **GitHub Actions** ejecuta el pipeline automáticamente
5. **Zero downtime** durante actualizaciones

### Demo en Vivo:
1. Mostrar código de la app
2. Hacer un cambio
3. Push a GitHub
4. Ver GitHub Actions ejecutándose
5. Mostrar app actualizada en maytebryon.com

## 📞 Contacto
Mayte - Estudiante DevOps

---
**⭐ Proyecto para demostrar CI/CD con Kubernetes**