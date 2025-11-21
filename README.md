# 🚀 CI/CD con Kubernetes - Proyecto Mayte

## 📖 Descripción
Proyecto de DevOps que demuestra CI/CD con Kubernetes

## 👩‍💻 Información
- **Estudiante**: Mayte
- **Cédula**: 1754347704
- **Materia**: DevOps

## 🛠️ Tecnologías
- Python + Flask
- Docker
- Kubernetes
- GitHub Actions

## 📦 Estructura
```
cicd-kubernetes-mayte/
├── app/
│   ├── app.py
│   └── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── Dockerfile
└── README.md
```

## 📊 Componentes de Kubernetes

### Pod
Unidad mínima que ejecuta contenedores

### Deployment
Gestiona réplicas y actualizaciones automáticas

### Service
Expone la aplicación y balancea tráfico

## 🚀 CI/CD
El pipeline automatiza:
1. Validación de código
2. Construcción de imagen Docker
3. Despliegue en Kubernetes

## ✨ Ventajas
- Automatización completa
- Alta disponibilidad
- Escalabilidad
- Auto-recuperación