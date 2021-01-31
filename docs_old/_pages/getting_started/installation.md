---
parent: Getting Started
title: "Installation"
---

Currently, Docker is required to run MMotH-Vent. Docker is a program that creates "containers" that allows code to be run in a controlled environment using the host computer's resources. A switch from Docker to Singularity may be made in the future to allow the code to be executed on a computing cluster. To get started, follow these steps:  
  * [Install Docker](#install-docker)
  * [Clone Repository](#clone-the-mmoth-vent-repository)
  * [Load Image](#load-image)
  * [Create Container](#create-container)
  * [Enter Container Command Line](#enter-container-command-line)

## Install Docker
Install the latest version of [Docker](http://www.docker.com).

## Clone the MMoth-Vent Repository
All of the source code to run MMotH-Vent is located on a [GitHub repository](https://github.com/mmoth-kurtis/MMotH-Fenics-UK.git). Users experienced with Git can do this through a command line approach. Otherwise, a .zip file from the repository can be downloaded. Unzip the file in the desired directory.

## Load Image  
A Docker image is a copy of the environment used to execute the code. This allows standardization of the modules and their versions used by MMoth-Vent. The image that needs to be loaded by Docker ~~is in the MMotH-Fenics-UK repository, saved as ```MMotH-Vent.tar```~~. *We need a way to distribute this outside of our lab* From the command line, with Docker running, navigate to where this file is saved on your machine, and execute the following:  
```
docker load < MMotH-Vent.tar
```
Note, this step takes time. Once the step is complete, execute:
```
docker images
```
to check that the ```MMotH-Vent``` image has been loaded correctly.


## Create Container
Once Docker has loaded the image, a container can be created in which MMoth-Vent will be executed. To access the cloned repository, the directory containing MMotH-Vent source code needs to be shared with the container. To create the container, and mount the directory to be shared, execute the following at the command line:  
```
sudo docker run -it --mount src=[/path_to_MMotH-Vent_directory_on_machine],target=[/home/fenics/shared/,type=bind image_name]
```
The directory structure within the new container is  
```
/home/  
|  +-- fenics/  
|  |  +-- demo/  
|  |  +-- local/  
|  |  +-- shared/  
```
and the contents of the MMotH-Vent will be located under the ```shared``` directory.  
Verify that the container has been created by executing the following at the command line:
```
docker ps -a
```
This displays something similar to the following, showing all containers created on the local machine.   
{% include figure image_path="/assets/images/docker_display_images.png" alt="Display containers" %}
Once the container has been created, it needs to be started. Use the following command and replace "Container ID" with the created container's ID which can be found from the previous command.
```
docker start [CONTAINER_ID]
```

## Enter Container Command Line
Now that the container is started, the following command takes the user to a command line within the container to execute the MMotH code. Replace CONTAINER_NAME with the name of the container as seen from the ```docker ps -a``` command.
```
sudo docker exec -ti -u fenics [CONTAINER_NAME] /bin/bash -l
```
It is recommended to create an alias shortcut to issue this command regularly. As a recap, once the container is created from the image, the regular workflow to use MMotH-Vent is:
* Start Docker
* From the command line, start the created container using ```docker start [CONTAINER_ID]```
* Enter the command line in the container using ```sudo docker exec -ti -u fenics [CONTAINER_NAME] /bin/bash -l```
The container can be exited by issuing the ```exit``` command. Continue to the next page to see how to run an MMotH-Vent simulation.

<a href="/MMotH-Vent/getting_started/running_demo/" class="btn btn--primary">Running a Simulation >></a>
