DevOps CI/CD Pipeline – GitHub → Docker Hub → Kubernetes

This repository demonstrates an end-to-end CI/CD pipeline that builds, packages, and deploys a Python Flask application to a Kubernetes cluster using an automated workflow.

Project Overview

This project implements a complete DevOps delivery workflow, including:
	•	Version control through GitHub
	•	Docker image build and tagging
	•	Publishing the image to Docker Hub
	•	Automated deployment to Kubernetes via kubectl
	•	Continuous rollout of new versions upon each push to the repository

The application itself is a minimal Flask-based “Hello World” web service, fully containerized and orchestrated via Kubernetes.

Architecture & Workflow

1. GitHub Repository

The application source code, Dockerfile, Kubernetes manifests, and CI/CD pipeline configuration are maintained in this repository.

2. Docker Image Build

The CI pipeline builds a Docker image using the provided Dockerfile, ensuring consistent runtime behavior.

3. Image Tagging and Publishing

Each build is tagged (typically using commit SHA or latest) and pushed to Docker Hub.

4. Kubernetes Deployment

After the image is pushed, the pipeline:
	•	Uses kubectl to create or update a Deployment
	•	Optionally exposes the application using a Kubernetes Service (NodePort or ClusterIP)

5. Automatic Rollout

Kubernetes performs a rolling update, ensuring zero downtime deployment of new application versions.

Technology Stack
	•	Python / Flask – Simple web service
	•	Docker – Containerization of the application
	•	Docker Hub – Image registry
	•	GitHub Actions – CI/CD automation
	•	Kubernetes (Minikube or cloud cluster) – Deployment platform
	•	kubectl – Cluster interaction and deployment updates

Folder Structure

./
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
├── deployment.yaml      # Kubernetes Deployment manifest (if included)
├── service.yaml         # Kubernetes Service manifest (optional)
└── .github/workflows/   # CI/CD pipeline definitions

Result

This pipeline successfully performs:
	•	Automated code retrieval
	•	Docker image generation and publishing
	•	Kubernetes deployment and rolling updates

Each commit to the repository triggers the entire pipeline, providing a reliable, production-ready DevOps workflow.

The deployed application is reachable from within the Kubernetes cluster (and externally if a Service is configured), confirming the complete CI/CD functionality from Git to Kubernetes.

How to Run Locally

Build the Docker image:

docker build -t <your-dockerhub-username>/flask-hello-world:latest .

Run the container:

docker run -p 5000:5000 <your-dockerhub-username>/flask-hello-world:latest

Then open:

http://localhost:5000

How to Deploy on Kubernetes

Apply the Deployment:

kubectl apply -f deployment.yaml

(Optional) Expose the app:

kubectl apply -f service.yaml


⸻

This project demonstrates a fully functional, automated CI/CD pipeline suitable for learning, demonstration, and foundational DevOps implementation.
