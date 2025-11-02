pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t devops-flask-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                docker run -d -p 8080:5000 --name flask-app devops-flask-app:latest
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                sleep 5
                curl http://localhost:8080
                '''
            }
        }
    }
}
