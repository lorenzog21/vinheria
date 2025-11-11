pipeline {
    agent any

    stages {
        stage('Build') {
    steps {
        echo "Iniciando build dos microsserviços..."
        sh 'echo "Build simulado dos microsserviços da Vinheria"'
    }
}

        }

        stage('Test') {
            steps {
                echo 'Executando testes simulados...'
                sh 'echo "Testes OK para Usuários e Catálogo"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Iniciando deploy da Vinheria...'
                sh 'mkdir -p /tmp/vino-publish'
                sh 'cp -r usuarios catalogo /tmp/vino-publish/'
                echo 'Deploy realizado em /tmp/vino-publish/'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizado com sucesso 🍷'
        }
        failure {
            echo 'Falha no pipeline 🚨'
        }
    }

