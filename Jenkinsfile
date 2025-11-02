pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'devops-flask-app'
        DOCKER_TAG = 'latest'
    }
    
    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }
        
        stage('Run') {
            steps {
                script {
                    // Stop any existing container
                    sh 'docker ps -q --filter "name=flask-app" | grep -q . && docker stop flask-app || true'
                    sh 'docker ps -aq --filter "name=flask-app" | grep -q . && docker rm flask-app || true'
                    
                    // Run the new container
                    sh 'docker run -d -p 8080:5000 --name flask-app $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Simple health check
                    sh 'curl -f http://localhost:8080 || exit 1'
                }
            }
        }
    }
}