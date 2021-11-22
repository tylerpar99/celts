pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo "pip install python"
                sh "setup.sh"
            }
        }
    stages{
    stage('Running python script'){
        sh  '''
            echo "executing python script"
            "'''+python_exec_path+'''" -m venv "'''+venv+'''" && "'''+venv+'''\\Scripts\\python.exe" -m pip install --upgrade pip && "'''+venv+'''\\Scripts\\pip" install -r "'''+pathToScript+'''\\requirements.txt" && "'''+venv+'''\\Scripts\\python.exe" "'''+pathToScript+'''\\my_script.py" --path "'''+PathFromJenkinsUI+'''"
            '''
    }
    }
    }
}
