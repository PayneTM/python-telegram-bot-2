pipeline {
    agent any

    options {
        skipStagesAfterUnstable()
    }
    
    environment {
        PRODUCT = 'bot'
        DOCKERHUB_CREDS = credentials('dockerhub-user')
    }

    stages {
        stage('Build') {
            steps {
                sh "docker build . -t ${env.PRODUCT}:${env.BUILD_ID} -t ${env.PRODUCT}:latest"
            }
        }

        stage('Dockerhub Login') {
            steps {
                sh "docker login -u ${env.DOCKERHUB_CREDS_USR} --password-stdin"
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
