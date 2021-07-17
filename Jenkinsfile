pipeline {
    environment {
        DB_PASSWORD = credentials("DB_URI")
    }
    stages {
        stage('Build') {
            steps {
                sh "docker-compose build"
                sh "export DB_PASSWORD"
            
            }
        }
        stage('Test') {
            steps {
                sh "cd service_1 && pytest test_server.py"
                sh "cd service_2_skill && pytest test_skill.py"
                sh "cd service_3_alliance && pytest test_alliance.py"
                sh "cd service_4_race && pytest test_race.py"
            }
        }
        stage('Deploy') {
            steps {
                sh "sudo docker stack services stack-1"
            }
        }
    }
}
