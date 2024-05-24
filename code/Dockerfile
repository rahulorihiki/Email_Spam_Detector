#The from command is used to fetch the base docker image and the latest here is a tag which means the latest version of alpine image
FROM alpine:latest
# python3-dev consist of both python3 as well as pip3 which is the base to run any flask application
RUN apk add --no-cache python3-dev 

RUN apk add --no-cache py3-pip
# 1. RUN command is used to run any command while the docker image is being created
# 2. apk is the package manager for alpine image
# 3. we have added a flag "--no-cache" because I dont want to get any cache stored to unnecessary increase the image size 
# 4. And we write "pip3 install --upgrade pip" to upgrade the pip which got installed along with python3-dev
# To run the docker file and to create a new image write docker build -t "name of the image" . // here the dot notation is used find the docker file present in the current folder
# to check write docker images to see all the docker images created and to see all the docker container running we write the command docker ps
# To run the docker image we write the command docker run -it "name of the image" /bin/sh through which we stay within the container without getting thrown outside it is like entering insode an environment and not getting kicked out of it like the default behaviour



