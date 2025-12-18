Flask CI/CD Pipeline – GitHub → Docker Hub → AWS EKS

Welcome to my DevOps project! This repository demonstrates a complete CI/CD pipeline for a Python Flask application, showcasing how code can flow from GitHub → Docker Hub → Kubernetes (AWS EKS) automatically.

About the Project

The goal of this project is to implement a hands-on, end-to-end DevOps workflow. It focuses on automation, security, and deployment best practices. The pipeline handles:
	•	Version control with GitHub – all code is stored and versioned in this repository.
	•	Docker containerization – the Flask app is packaged as a Docker image.
	•	Image security scanning – Trivy is used to scan the Docker image for vulnerabilities.
	•	Docker Hub registry – images are pushed and versioned on Docker Hub.
	•	Kubernetes deployment on AWS EKS – Helm charts manage deployment and service configuration.
	•	Automatic updates – each commit to the main branch triggers the entire pipeline.

The Flask app itself is simple (“Hello World”), so the focus is entirely on CI/CD automation rather than application complexity.


How the Pipeline Works
	1.	GitHub Repository
	•	All source code, Dockerfile, and Helm charts are stored here.
	•	Any push to the main branch triggers the GitHub Actions workflow.
	2.	Docker Build & Trivy Scan
	•	A Docker image is built for the Flask app.
	•	Trivy scans the image for high and critical vulnerabilities.
	3.	Docker Push
	•	The validated Docker image is pushed to Docker Hub.
	4.	Kubernetes Deployment with Helm
	•	The pipeline updates the kubeconfig to connect to AWS EKS.
	•	Helm manages deployment, ensuring the app is running smoothly.
	5.	Accessing the App
	•	The workflow outputs the public URL where the Flask app can be accessed.
	•	This confirms that the application is live and up-to-date.

Technology Stack
	•	Python / Flask – web application
	•	Docker – containerization
	•	Docker Hub – image registry
	•	GitHub Actions – CI/CD workflow automation
	•	AWS EKS – Kubernetes cluster
	•	Helm – deployment management
	•	Trivy – image vulnerability scanning

	
Project Structure

./
├── app.py             # Flask application
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker image build instructions
├── helm/              # Helm charts for deployment
│   └── flask-app
├── .github/workflows/ # CI/CD pipeline definition
└── README.md          # Project documentation

Result

With this pipeline, any code change is automatically built, scanned, pushed, and deployed to Kubernetes on AWS EKS. It demonstrates a real-world DevOps workflow, showing how continuous integration and deployment can be fully automated, secure, and reliable.
