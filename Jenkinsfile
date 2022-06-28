pipeline {
    agent any

    options {
        skipStagesAfterUnstable()
    }
    
    environment {
        PRODUCT = 'paynetm/devops-test'
    }

    stages {
        stage('Build') {
            environment {
                CONFIG_FILE_ID = credentials('main_config')
            }
            steps {
                sh "cp --remove-destination ${CONFIG_FILE_ID} ."
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
