pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/rizalamrirozaqi/inventory-app.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t inventory-app .'
      }
    }

    stage('Test') {
      steps {
        sh 'pytest --junitxml=test-results.xml tests/'
      }
    }
    post {
      always {
        junit 'test-results.xml'
      }
    }

    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv('My SonarQube Server') {
          sh 'sonar-scanner'
        }
      }
    }

    stage('Push Docker') {
      steps {
        sh 'docker tag inventory-app rizalamri/inventory-app:latest'
        sh 'docker push rizalamri/inventory-app:latest'
      }
    }

    stage('Deploy to Minikube') {
      steps {
        sh 'kubectl apply -f deployment.yaml'
      }
    }
  }
}