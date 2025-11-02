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
                // Stop and remove any existing container
                bat '''
                docker stop flask-app 2>nul || exit /b 0
                docker rm flask-app 2>nul || exit /b 0
                docker run -d -p 8080:5000 --name flask-app devops-flask-app:latest
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                timeout 5
                curl http://localhost:8080
                '''
            }
        }
    }
}
