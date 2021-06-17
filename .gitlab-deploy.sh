#!/bin/bash

#Get servers list
set -f
string=$AWS_IP
array=(${string//,/ })

for i in "${!array[@]}"; do
  echo "Deploying information to EC2 and Gitlab"
  echo "Deploy project on server ${array[i]}"
  ssh ubuntu@${array[i]}  "cd django-recipe-api && git pull origin main && sudo docker-compose build && kubectl create -f Kubernetes/deployment.yml && kubectl create -f Kubernetes/service.yml "
done 