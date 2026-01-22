Flask CI/CD Pipeline on AWS EKS

This project demonstrates a complete CI/CD pipeline for a Flask application, deployed to AWS EKS, using GitHub Actions.
The focus of this repository is automation — from code push to a running application in Kubernetes.


What This Project Does:

Every time code is pushed to the main branch, the pipeline automatically:
	1.	Builds a Docker image for the Flask app
	2.	Scans the image for vulnerabilities using Trivy
	3.	Pushes the image to Docker Hub
	4.	Connects securely to AWS EKS
	5.	Deploys the application using Helm
	6.	Applies the Argo CD application manifest
	7.	Verifies the deployment and prints the access URL
No manual steps are required.

CI/CD Flow:
GitHub Push
   ↓
Docker Build
   ↓
Trivy Security Scan
   ↓
Docker Hub Push
   ↓
Helm Deployment
   ↓
AWS EKS

Technology Stack:
	•	Flask – Python web application
	•	Docker – Containerization
	•	Docker Hub – Container registry
	•	GitHub Actions – CI/CD automation
	•	AWS EKS – Kubernetes cluster
	•	Helm – Kubernetes package manager
	•	Trivy – Image vulnerability scanning
	•	Argo CD – Kubernetes application configuration

Repository Structure:
  .
├── app.py
├── Dockerfile
├── requirements.txt
├── helm/
│   └── flask-app/
├── argocd/
│   └── flask-app.yaml
├── .github/workflows/
│   └── ci-cd.yaml
└── README.md

Deployment Details:
	•	Docker images are tagged as latest
	•	The Kubernetes deployment is managed via Helm
	•	The service is exposed using NodePort
	•	Argo CD manifests are applied as part of the pipeline
	•	The workflow prints the service URL after deployment

Accessing the Application:
After a successful pipeline run, the workflow outputs:
Flask app should be accessible at http://<NODE_IP>:<NODE_PORT>
This URL can be used to verify that the application is running.
