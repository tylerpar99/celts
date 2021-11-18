pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                // 
            }
        }
        stage("test PythonEnv") {
            steps{
            withPythonEnv('python3') {
                sh 'pip install pytest'
                sh 'pytest mytest.py'
            }
    }
}
    }
}
