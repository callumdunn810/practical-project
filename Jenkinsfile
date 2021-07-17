pipeline {
    agent any
    environment {
        DATABASE_PASSWORD = credentials('DATABASE_URI')
        DATABASE_URI='mysql+pymysql://root:Grg170dx@34.105.231.190:3306/generatedb'
    }
    stages {
        stage('Build') {
            steps {
                sh "export DATABASE_PASSWORD"
                sh "docker-compose build"
                
            
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
