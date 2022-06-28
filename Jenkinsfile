pipeline {
    agent any

    options {
        skipStagesAfterUnstable()
    }
    
    environment {
        PRODUCT = 'bot'
    }

    stages {
        stage('Build') {
            steps {
                sh "docker build . -t ${env.PRODUCT}:${env.BUILD_ID} -t ${env.PRODUCT}:latest"
            }
        }

        stage('Dockerhub Login') {
             environment {
                DOCKERHUB_CREDS = credentials('dockerhub-user')
            }
            steps {
                sh "docker login -u ${env.DOCKERHUB_CREDS_USR} -p ${env.DOCKERHUB_CREDS_PSW}"
            }
        }

        stage('Push') {
            steps {
                sh "docker push -a ${env.PRODUCT}"
            }
        }
    }
    post{
        always
        {
            sh "docker logout"
        }
    }
}
