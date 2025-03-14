#!/bin/bash

# Build a docker container
docker build -t transcriber-image .

# Start the container
docker run -p 5001:5001 --name transcriber transcriber-image
