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
                    bat "docker build -t %DOCKER_IMAGE%:%DOCKER_TAG% ."
                }
            }
        }
        
        stage('Run') {
            steps {
                script {
                    // Stop and remove existing container if it exists
                    bat "docker stop flask-app 2>nul || exit /b 0"
                    bat "docker rm flask-app 2>nul || exit /b 0"
                    
                    // Run the new container
                    bat "docker run -d -p 8080:5000 --name flask-app %DOCKER_IMAGE%:%DOCKER_TAG%"
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Simple health check with retry
                    bat "ping localhost -n 5"
                    bat "curl http://localhost:8080"
                }
            }
        }
    }
    
    post {
        failure {
            echo 'Pipeline failed! Check the logs for details.'
        }
        success {
            echo 'Pipeline succeeded! Application is running at http://localhost:8080'
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