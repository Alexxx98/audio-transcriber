#!/bin/bash

# Stop and remove container
docker stop transcriber
docker remove transcriber

# Build image and run container
docker build -t transcriber-image .
docker run -p 5001:5001 --name transcriber transcriber-image
