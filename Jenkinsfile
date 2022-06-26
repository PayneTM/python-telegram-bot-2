pipeline {
    agent any

    options {
        skipStagesAfterUnstable()
    }

    stages {
         stage('Build') { 
            agent {
                docker {
                    image 'python:3' 
                }
            }
            steps {
                sh 'python -m py_compile main.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/blah'
                IMAGE = 'cdrx/pyinstaller-linux:python2'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F main.py'"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/main"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}
