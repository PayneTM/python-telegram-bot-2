pipeline {
    agent any

    stages {
         stage('Build') { 
            agent {
                docker {
                    image 'python:3' 
                }
            }
            steps {
                sh 'python -m py_compile *.py*' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}
