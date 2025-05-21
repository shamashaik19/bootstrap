pipeline{
    agent any
    stages{
        stage('git checkout') {
            steps {
                git url: "https://github.com/shamashaik19/bootstrap.git"
            }
        }
        stage('compile project') {
            steps {
                sh "mvn compile"
            }
        }
        stage('test project') {
            steps {
                sh "mvn test"
            }
        }
        stage('package'){
            steps {
                sh "mvn package"
            }
        }
        stage('Generate Test HTML Report') {
            steps {
                sh "mvn surefire-report:report-only"
            }
         }
        stage('Publish Test Reports') {
            steps {
                publishHTML([
                    allowMissing: true, 
                    alwaysLinkToLastBuild: true, 
                    keepAll: true, 
                    reportDir: 'target/site', 
                    reportFiles: 'surefire-report.html', 
                    reportName: 'HTML Report'
                ])
            }
        }
        stage('Containerize the Application') {
            steps {
                echo 'Creating Docker image...'
                sh "docker build --no-cache -t shamashaik19/freelancerimage:latest ."
            }
        }
        stage('Push to DockerHub') {
            steps {
                echo 'Pushing the Docker image to DockerHub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-pwd', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push shamashaik19/freelancerimage:latest"
                }
            }
        }
        stage('Configure and Deploy to Test Server') {
            steps {
                echo 'Deploying application using Ansible...'
                ansiblePlaybook(
                    become: true,
                    credentialsId: 'ansible-key',
                    disableHostKeyChecking: true,
                    installation: 'ansible',
                    inventory: '/etc/ansible/hosts',
                    playbook: 'playbook.yml'
                )
            }
        }
    }
}
