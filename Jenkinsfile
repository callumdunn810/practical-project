pipeline{
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')
    }
    stages{
        stage('Build') {
            steps{
                sh "export 'DATABASE_URI'=${DATABASE_URI}"
                sh "docker pull callumdunn810/service_1"
                sh "docker pull callumdunn810/service_2_skill"
                sh "docker pull callumdunn810/service_3_alliance"
                sh "docker pull callumdunn810/service_4_race"
            }
        }
        stage('Test') {
            steps {
            }
        }
        stage('Deploy'){
            steps{
                sh "sudo docker stack services stack-1"
            }
        }
    }
}

