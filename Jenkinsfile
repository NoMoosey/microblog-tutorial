pipeline {

  agent any
  
  stages {
  
    stage("build") {
    
      steps {

        echo 'This is the build stage!'
        echo 'That was auto-triggered?'
        echo 'Build should be fixed!'
      
      } 
    }

    stage("test") {
    
      steps {

        echo 'This is the test stage!'
      
      } 
    }

    stage("deploy") {
    
      steps {

        echo 'This is the deploy stage!'
      
      } 
    }
  }
}