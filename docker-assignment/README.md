# Dockerized Python Application

## Overview
This is a Dockerized Python Flask application following security best practices and optimization techniques.

## Features
- Multi-stage builds for optimized image size
- Non-root user for enhanced security
- Health check endpoints
- Proper layer caching
- Resource monitoring

## Build Instructions

### Prerequisites
- Docker installed
- Python 3.8+

### Building the Image
```bash
docker build -t myapp:1.0 .

### Running the Container
docker run -d -p 8080:8080 --name myapp-container myapp:1.0

### Testing Endpoints
# Health check
curl http://localhost:8080/health

# GET endpoint
curl http://localhost:8080/GET

### Monitoring
# View logs
docker logs myapp-container

# Resource usage
docker stats myapp-container

### Publishing
#DockerHub
docker tag myapp:1.0 username/myapp:1.0
docker push username/myapp:1.0

### AWS ECR
aws configure
docker build -t myapp:1.0 .
docker tag myapp:1.0 211125429897.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0
docker push 211125429897.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0
