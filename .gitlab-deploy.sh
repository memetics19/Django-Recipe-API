#!/bin/bash

#Get servers list
set -f
string=$AWS_IP
array=(${string//,/ })

for i in "${!array[@]}"; do
  echo "Deploying information to EC2 and Gitlab"
  echo "Deploy project on server ${array[i]}"
  ssh ubuntu@${array[i]}  "cd django-recipe-api && sudo docker build  -t docsify/demo . &&  sudo docker run -itp 3000:3000 --name=docsify "
done 