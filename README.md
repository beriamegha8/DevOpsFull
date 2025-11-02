# DevOps Assignment Project

This project demonstrates a simple DevOps pipeline using Docker, Jenkins, and Kubernetes.

## Project Structure
```
├─ app.py               # Flask application
├─ requirements.txt     # Python dependencies
├─ Dockerfile          # Container configuration
├─ Jenkinsfile         # CI/CD pipeline
├─ deployment.yaml     # Kubernetes deployment
└─ README.md          # This file
```

## Task 1: Docker + Jenkins Mini Pipeline

### Prerequisites
- Docker installed
- Jenkins installed and running in Docker
- Jenkins Docker plugin installed

### Steps

1. Start Jenkins:
```bash
docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home --name jenkins jenkins/jenkins:lts
```

2. Get Jenkins initial password:
```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

3. Configure Jenkins:
- Access Jenkins at http://localhost:8080
- Install suggested plugins
- Create admin user
- Create new pipeline job using the Jenkinsfile

4. Run the pipeline:
- The pipeline will build and run the Flask application
- Access the app at http://localhost:8080

## Task 2: Kubernetes Deployment

### Prerequisites
- Kubernetes cluster (e.g., minikube)
- kubectl configured

### Steps

1. Apply the deployment:
```bash
kubectl apply -f deployment.yaml
```

2. Verify deployment:
```bash
kubectl get pods
kubectl get svc
```

3. Access the application:
- The service will be available at `http://[node-ip]:30000`

## Task 3: Security Scan with Trivy

### Steps

1. Install Trivy:
```bash
brew install trivy  # macOS
# or
sudo apt-get install trivy  # Ubuntu
```

2. Scan the Docker image:
```bash
trivy image devops-flask-app:latest
```

3. Review the security report in the terminal output.

## Common Issues and Solutions

1. If Jenkins container fails to start:
   - Check if port 8080 is already in use
   - Ensure Docker has sufficient permissions

2. If Kubernetes pods are not running:
   - Check pod logs: `kubectl logs [pod-name]`
   - Verify image pull policy and image name

3. If Trivy scan fails:
   - Ensure Docker image is built and available locally
   - Check Trivy installation

## GitHub Repository
https://github.com/beriamegha8/DevOpsFull