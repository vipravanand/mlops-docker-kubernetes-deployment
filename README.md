## Project Overview

-Build a docker container for a gunicorn-embedded flask app to serve model prediction using a pre-trained tensoprflow model

-Deploy the container on a Google CLoud Kubernetes Engine as a Kuberneted Service

-Configure the Kubernetes Cluseter for Horizontal Pod Scaling and Vertical Autoscaling

-Load Test the kubernetes service using locust

Note  ; Pretrained model is a AutoEncoder Tensorflow model configured to act as a Anomaly Detector based on MAE ( Mean Absolute Error) based threshold)


### Building Docker Container and Publishing to GCR

Dockerfile is built by specifyinf the required base image and requirements and CMD for execution

The repo is clones using google cloud shell 

The docker image is build in cloud shell using gcloud builds command and a image is published to gcr ( google cloud registry) 

The gcr image path is extracted and specification in deployment.yaml


### Building Kubernetes Service

Kubernetes cluster is created specifing the cluster name, compute/zone, machine type, enabling autoscaling , and min nodes, max nodes, and num_nodes while starting

Using kubectl, deployment.yaml is used to build a deployment and service,yaml builds a load balancing service for the deployment

The horizontal pod scaler is configured mentioning the CPU utilisation threshold and min and max number of pods. 

External IP of the service is used as endpoint for the prediction requests

### Load Test

Locust task is initiated configuring the number of users and spawning rate of uses to make requests on the model prediction service. 

As load is gradually increase, pods are horizontally scaled and with further increase in the load as per the horizontal pod autoscaler config, number of nodes imcreases as the max_nodes parameter defined while creating cluster

Autoscaling Ensures that pods and nodes are scaled back as load decreases. 


## File System : 

AEFlask.py - Defines the flask app

AEgunicorn - for multithreading the flask app using gunicorn

autoencoder.hdf5 - pretrained tensforfow model

Dockerfile - for building the docker image for the flask app 

requirements.txt - specfies the dependencies 

loadtest.py - specifies the task for the load testing of the endpoint 

deployment.yaml - configuration for building kubernetes deployment for the docker container 

service.yaml - configuratin for the deployment of the container as a kubernetes service

