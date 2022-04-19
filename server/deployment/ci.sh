#!/usr/bin/env bash

PYTHON_PACKAGES="black pylint"
cd ./server

if [[ "$1" == "--no-step-0" ]]; then
  echo -e "=== Skiping python packages install"
else
  echo -e "=== Step 0 install requirements ==="

  for package in $PYTHON_PACKAGES; do 
    exist=$(pip list | grep -F $package | wc -l)
    if [[ $exist -eq "0" ]]; then
      pip install $package
    fi
  done
fi

echo -e "\n\n==== Step 1 One Lint and Format ===="

echo -e "Formating ..."
python3 -m black --check main.py

echo -e "Linting ..."
python3 -m pylint main.py

echo -e "\n\n==== Step 2 Build docker image ===="

DOCKER_IMAGE_TAG=$(git rev-parse --short HEAD)

# Making sure the image is store in the minikube docker engine as we do not have an external registry
eval $(minikube docker-env)
docker build -t gameserver:$DOCKER_IMAGE_TAG .

echo -e "\n\n==== Step 3 Deploy helm chart ===="

cd deployment
# Here we should create a new release of the helm chart but since we don't have a registry like chartmuseum
terraform apply -auto-approve
