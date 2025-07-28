pipeline {
    agent {
        docker {
            image 'python:3.10' 
        }
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/rizalamrirozaqi/inventory-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'pytest tests/test_item.py --junitxml=unit-report.xml'
            }
        }

        stage('Run Integration Tests') {
            steps {
                sh 'python app/main.py &'
                sh 'sleep 5'
                sh 'pytest tests/test_integrasi.py --junitxml=integration-report.xml'
            }
        }

        stage('Publish Reports') {
            steps {
                junit 'unit-report.xml'
                junit 'integration-report.xml'
            }
        }
    }

    post {
        success {
            echo 'All tests passed.'
        }
        failure {
            echo 'Test failed.'
        }
    }
}
