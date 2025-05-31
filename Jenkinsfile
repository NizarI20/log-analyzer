pipeline {
  agent any
  stages {
    stage('Start') {
      steps {
        echo 'Début de l’analyse des logs'
      }
    }
    stage('Analyze') {
      steps {
        sh 'python log_analyzer.py'
        sh 'cat rapport.txt'
      }
    }
    stage('Check Errors') {
      steps {
        script {
          def content = readFile('rapport.txt')
          def errorCount = content.count('ERROR')
          echo "Nombre d'erreurs : ${errorCount}"
          if (errorCount > 5) {
            error("Échec : trop d'erreurs")
          }
        }
      }
    }
    stage('End') {
      steps {
        echo 'Fin du pipeline'
      }
    }
  }
}
