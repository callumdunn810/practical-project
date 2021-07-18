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
                sh "sudo apt update"
                sh "sudo apt install python3-pip3"
                sh "sudo apt install python3-venv"
                sh "python3 -m venv venv"
                sh ". ./venv/bin/activate && pip3 install -r requirements.txt && pytest --version && pip3 install Flask-Testing"
            }
        }
        stage('Test') {
            steps {
                sh ". ./venv/bin/activate && dc service_1 && python3 -m pytest test.py"
                sh "cd service_1 && pytest test_server.py"
                sh "cd service_2_skill && pytest test_skill.py"
                sh "cd service_3_alliance && pytest test_alliance.py"
                sh "cd service_4_race && pytest test_race.py"
            }
        }
        stage('Deploy'){
            steps{
                sh "docker stack deploy --compose-file docker-compose.yaml character"
            }
        }
    }
}

