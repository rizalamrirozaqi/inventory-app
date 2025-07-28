pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/rizalamrirozaqi/inventory-app.git'
      }
    }

    stage('Install Requirements') {
      steps {
        sh 'python3 --version'
        sh 'pip3 install -r requirements.txt'
      }
    }

    stage('Run Tests') {
      steps {
        sh 'pytest tests/'
      }
    }
  }
}
