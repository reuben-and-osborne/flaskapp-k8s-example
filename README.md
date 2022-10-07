# flaskapp-k8s-example

## Build & run using Docker

build:
`docker build --tag flask-app-docker .` 

run:
`docker run flask-app-docker`

run detached:
`docker run -d -p 5000:5000 flask-app-docker`
