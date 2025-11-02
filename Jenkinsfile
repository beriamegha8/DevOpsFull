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
                docker network create flask-net || true
                docker stop flask-app || true
                docker rm flask-app || true
                docker run -d --network flask-net -p 8081:5000 --name flask-app devops-flask-app:latest
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                sleep 5
                docker exec flask-app curl http://localhost:5000
                '''
            }
        }
    }
}
