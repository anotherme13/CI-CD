pipeline{
  agent any
  environment{
    VENV = 'venv'
    DOCKER_IMAGE = 'test-flask'
    CONTAINER_NAME = 'test-flask-container'
  }
  stages{
    stage('Cleanup Previous Build'){
      steps{
        script {
          try {
            bat 'docker stop %CONTAINER_NAME%'
            bat 'docker rm %CONTAINER_NAME%'
          } catch (Exception e) {
            echo "No previous container to cleanup"
          }
        }
      }
    }
    stage('Prepare Environment'){
      steps{
        bat 'if exist %VENV% rmdir /s /q %VENV%'
        bat 'python -m venv %VENV%'
        bat '%VENV%\\Scripts\\python -m pip install --upgrade pip'
        bat '%VENV%\\Scripts\\pip install -r requirements.txt'
      }
    }
    stage('Run Tests'){
      steps{
        bat '%VENV%\\Scripts\\python -m unittest discover -s tests'
      }
    }
    stage('Build Docker Image'){
      steps{
        bat 'docker build -t %DOCKER_IMAGE% .'
      }
    }
    stage('Deploy Application'){
      steps{
        bat 'docker run -d --name %CONTAINER_NAME% -p 5000:5000 %DOCKER_IMAGE%'
        sleep 5
        script {
          try {
            bat 'curl -f http://localhost:5000/health'
            echo "Application deployed successfully and health check passed"
          } catch (Exception e) {
            error "Health check failed - deployment unsuccessful"
          }
        }
      }
    }
  }
  post {
    always {
      echo 'Pipeline completed'
    }
    success {
      echo 'Pipeline succeeded!'
    }
    failure {
      echo 'Pipeline failed!'
      script {
        try {
          bat 'docker stop %CONTAINER_NAME%'
          bat 'docker rm %CONTAINER_NAME%'
        } catch (Exception e) {
          echo "Failed to cleanup container"
        }
      }
    }
  }
}

