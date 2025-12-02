DevOps CI/CD Pipeline – GitHub → Docker Hub → Kubernetes

Welcome to my DevOps project! This repository showcases a full CI/CD pipeline that takes a simple Python Flask application from GitHub, packages it in Docker, and deploys it to a Kubernetes cluster automatically.

About the Project

The goal of this project was to implement a hands-on, end-to-end DevOps workflow. It covers:
	•	Version control with GitHub
	•	Building and tagging a Docker image for a Flask web app
	•	Pushing the Docker image to Docker Hub
	•	Deploying the app to Kubernetes using kubectl
	•	Automatically updating the deployment whenever code changes are pushed

The app itself is a lightweight “Hello World” Flask service, but the focus here is on the automation pipeline.

How the Pipeline Works
	1.	GitHub Repository: All source code, Dockerfile, and Kubernetes manifests are stored here.
	2.	Docker Build & Push: Each commit triggers the build of a Docker image, which is then pushed to Docker Hub.
	3.	Kubernetes Deployment: The pipeline applies the Deployment and Service manifests using kubectl, ensuring that the latest version is running in the cluster.

Technology Stack
	•	Python / Flask – web application
	•	Docker – containerization
	•	Docker Hub – image registry
	•	GitHub Actions – automation of CI/CD pipeline
	•	Kubernetes – container orchestration
	•	kubectl – command-line cluster management

Project Structure

./
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Instructions to build the Docker image
├── deployment.yaml      # Kubernetes Deployment manifest
├── service.yaml         # Kubernetes Service manifest
└── .github/workflows/   # CI/CD pipeline definitions

Running Locally

Build the Docker image:

docker build -t <your-dockerhub-username>/flask-hello-world:latest .

Run the container:

docker run -p 5000:5000 <your-dockerhub-username>/flask-hello-world:latest

Then open your browser at http://localhost:5000 to see the app.

Deploying to Kubernetes

Apply the Deployment:

kubectl apply -f deployment.yaml

(Optional) Apply the Service:

kubectl apply -f service.yaml

Result

This pipeline fully automates the workflow from code changes in GitHub to a running application in Kubernetes. Every commit triggers the process, producing a Docker image, pushing it to Docker Hub, and updating the Kubernetes deployment without downtime. It’s a small but complete demonstration of DevOps principles in action.

⸻

I hope this gives you a clear picture of how CI/CD can streamline application delivery and management. Enjoy exploring the pipeline!
