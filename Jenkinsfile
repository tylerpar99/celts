pipeline {
    agent any 
    stage("test PythonEnv") {

    withPythonEnv('python3') {
        sh 'pip install pytest'
        sh 'pytest test_course_management.py'
    }
}
}
