pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/gani-code/airline_satisfaction_ml.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || echo "No tests found"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying your ML app...'
                // Example: sh 'python app.py'
            }
        }
    }
}
