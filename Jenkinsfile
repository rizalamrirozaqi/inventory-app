pipeline {
  agent {
    docker {
      image 'python:3.10-slim'
    }
  }

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/rizalamrirozaqi/inventory-app.git'
      }
    }

    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Run Tests') {
      steps {
        sh 'pytest tests/'
      }
    }

    stage('Build Docker') {
      steps {
        sh 'echo Building Docker Image...'
        // Optional: Build image if Docker-in-Docker enabled
        // sh 'docker build -t inventory-app .'
      }
    }
  }

  post {
    success {
      echo 'Pipeline finished successfully!'
    }
    failure {
      echo 'Pipeline failed. Check the logs.'
    }
  }
}
