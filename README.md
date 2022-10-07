# flask_with_k8s


Launch locally with k8s:

Prerequisites:
1. Docker desktop installed
2. Minikube installed

Start local k8s:
2. Run minikube: 'minikube start'
3. Launch dashboard: 'minikube dashboard'

Load Image to minikube:
1. Build image: 'docker-compose build <service_name>'
2. Load image: 'minikube image load <image_name>' (get it from 'docker image ls')

Create application and services:
1. Type 'kubectl apply -f C:\Users\Ran\PycharmProjects\FlaskWithGithubActions\k8s\deployment.yml' (to spin up pod containing image)
2. Type 'kubectl apply -f C:\Users\Ran\PycharmProjects\FlaskWithGithubActions\k8s\service.yml' (to enable communication with flask service)
3. Type 'kubectl apply -f C:\Users\Ran\PycharmProjects\FlaskWithGithubActions\k8s\ingress.yml' (to enable localhost communication with flask service)
Note: you should enable the ingress addon first before executing step 3 - to do that type: 'minikube addons enable ingress'
4. Type 'kubectl get ing' to get ingress ip or go to k8s dashboard > services > ingress > under the Endpoint column
- now you shuold get the response from the flask app
