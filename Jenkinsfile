pipeline {
    agent any 
    stages {
        stage('Static Analysis') {
            steps {
                echo 'Run the static analysis to the code' 
            }
        }
        stage("test PythonEnv") {

    withPythonEnv('python3') {
        sh 'pip install pytest'
        sh 'pytest mytest.py'
    }
}
    }
}
