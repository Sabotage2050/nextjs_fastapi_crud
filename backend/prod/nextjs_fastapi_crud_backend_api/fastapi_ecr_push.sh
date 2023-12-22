#!/bin/bash

GIT_COMMIT_ID=$(git log --format="%H" -n 1)
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 724871381121.dkr.ecr.ap-northeast-1.amazonaws.com/fastapi-nextjs-crud-todo-backend-fastapi
docker build -t fastapi-nextjs-crud-todo-backend-fastapi:"${GIT_COMMIT_ID}" -f ./prod/fastapi/Dockerfile.prod ./prod/fastapi
docker tag fastapi-nextjs-crud-todo-backend-fastapi:"${GIT_COMMIT_ID}" 724871381121.dkr.ecr.ap-northeast-1.amazonaws.com/fastapi-nextjs-crud-todo-backend-fastapi:"${GIT_COMMIT_ID}"
docker push 724871381121.dkr.ecr.ap-northeast-1.amazonaws.com/fastapi-nextjs-crud-todo-backend-fastapi:"${GIT_COMMIT_ID}"
