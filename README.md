Flask CI/CD Pipeline with Docker, Helm, EKS, and Argo CD

This repository contains an end-to-end CI/CD and GitOps-oriented deployment pipeline for a Dockerized Flask application running on AWS EKS

The project demonstrates how to:
- Build and scan container images in CI
- Publish images to Docker Hub
- Deploy applications to Kubernetes using Helm
- Synchronize cluster state using Argo CD (GitOps)

Purpose of This Project:

The goal of this repository is to demonstrate DevOps and Platform Engineering practices, including:

- Continuous Integration using GitHub Actions
- Container security scanning with Trivy
- Kubernetes application packaging with Helm
- GitOps-style deployment using Argo CD
- Cloud-native deployment on AWS EKS

This project is suitable for:
- Learning CI/CD and GitOps concepts
- Kubernetes and Helm hands-on practice

Architecture: 
Developer ( git push )-> GitHub Actions (CI) -> Docker Build & Security Scan -> Docker Hub (Image Registry) -> Helm Chart (Kubernetes Manifests) -> Argo CD (GitOps Sync) -> AWS EKS Cluster -> Flask Application (Kubernetes)
