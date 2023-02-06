# G42cloud-sre-assignment-shivam-shah-submission

This is a flask application to store and retrieve the population of cities using Elasticsearch as the database. The application has four API endpoints:

1.  `/health` to check the health of the application
2.  `/city/population` to add or update the population of a city
3.  `/city` to get the population of all cities
4.  `/city/<city_name>/population` to get the population of a specific city

## Prerequisites

1. Minikube (or kuberenetes cluster) 
2. Docker

## Installation

1.  Clone the repository

`git  clone  https://github.com/<repository_url>.git`

2.  Start minikube cluster 

`minikube start --cpus=4 --memory=6144`

## Deployment

1.  Build the Docker image and store it in minikubes internal registry

`minikube image build -t g42-python-app .`

2.  Deploy elastic-search application

`helm install elasticsearch ./elasticsearch`

Note: Wait for the pods to be in Ready state.

3.  Deploy the python Application

`helm install flask-app ./charts`

4.  Expose the flask-application endpoint to test it locally

`kubectl port-forward --namespace default svc/g42-sre-flask-app 5000:5000`

5.  Test the application

`curl http://localhost:5000/health`

## API Endpoints

### 1. /health

#### Method: GET

This endpoint is used to check the health of the application.

#### Response

`{  "status":  "OK"  }`

### 2. /city/population

#### Method: POST, PUT

This endpoint is used to add or update the population of a city.

#### Request Body

json

`{  "city":  "<city_name>",  "population":  <population>  }`

#### Response

`{  "status":  "Success"  }`

### 3. /city

#### Method: GET

This endpoint is used to get the population of all cities.

#### Response

`[ {  "city":  "<city_name>",  "population": <population> }, ...]`

### 4. /city/<city_name>/population

#### Method: GET

This endpoint is used to get the population of a specific city.

#### Response

`{  "city":  "<city_name>",  "population":  <population>  }`



