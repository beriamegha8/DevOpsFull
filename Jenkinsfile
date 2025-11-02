pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t devops-flask-app:latest .'
            }
        }
        
        stage('Deploy') {
            steps {
                bat 'docker stop flask-app 2>nul || exit /b 0'
                bat 'docker rm flask-app 2>nul || exit /b 0'
                bat 'docker run -d -p 8080:5000 --name flask-app devops-flask-app:latest'
            }
        }
        
        stage('Test') {
            steps {
                bat 'timeout 5'
                bat 'curl http://localhost:8080'
            }
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