pipeline {
  agent any

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
        sh 'docker build -t inventory-app .'
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
