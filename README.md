# flask_with_k8s


Launch locally with k8s:

Prerequisites:
1. Docker desktop installed
2. Minikube installed

Start local k8s:
1. Run minikube: 'minikube start'
2. Launch dashboard: 'minikube dashboard'

Load Image to minikube:
1. Build image: 'docker-compose build <service_name>'
2. Load image: 'minikube image load <image_name>' (get it from 'docker image ls')

Create application and services:
1. Type 'kubectl apply -f <path_to_deployment_file>' (to spin up pod containing image)
2. Type 'kubectl apply -f <path_to_service_file>' (to enable communication with flask service)
3. Type 'kubectl apply -f <path_to_ingress_file>' (to enable localhost communication with flask service)
- Note: you should enable the ingress addon first before executing step 3 - to do that type: 'minikube addons enable ingress'
4. Type 'kubectl get ing' to get ingress ip or go to k8s dashboard > services > ingress > under the Endpoint column
- Now you shuold get the response from the flask app

Project Resources:
1. Deploying a Flask Application on Kubernetes | Practical K8s Overview (https://www.youtube.com/watch?v=-g9r8BSlDFI)
