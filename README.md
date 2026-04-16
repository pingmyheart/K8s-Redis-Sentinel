# K8s-Redis-Sentinel

*Minimal configuration with managed edge cases to deploy redis sentinel in kubernetes cluster*

![Last Commit](https://img.shields.io/github/last-commit/pingmyheart/K8s-Redis-Sentinel)
![Repo Size](https://img.shields.io/github/repo-size/pingmyheart/K8s-Redis-Sentinel)
![Issues](https://img.shields.io/github/issues/pingmyheart/K8s-Redis-Sentinel)
![Pull Requests](https://img.shields.io/github/issues-pr/pingmyheart/K8s-Redis-Sentinel)
![License](https://img.shields.io/github/license/pingmyheart/K8s-Redis-Sentinel)
![Top Language](https://img.shields.io/github/languages/top/pingmyheart/K8s-Redis-Sentinel)
![Language Count](https://img.shields.io/github/languages/count/pingmyheart/K8s-Redis-Sentinel)

## Overview

This repository provides a minimal configuration to deploy Redis Sentinel in a Kubernetes cluster. It includes handling
of managed edge cases to ensure a robust and reliable deployment.

## Architecture

Deployment consists of a Redis Sentinel setup with the following components:

- **1 Redis Master**: The primary Redis instance that handles write operations.
- **2 Redis Replicas**: Secondary Redis instances that replicate data from the master and handle read operations.
- **3 Redis Sentinel**: A monitoring system that detects failures and promotes replicas to master when necessary.

This architecture ensures high availability and fault tolerance for the Redis deployment and follows official Redis
Sentinel best practices.

## Repository Structure

- `/app/redis/deploy` - Contains the deployment YAML file
- `/app/redis/service` - Contains the service YAML file
- `/environment-config` - Contains environment configuration files for the deployment
- `/environment-config/config/redis.yaml` - Contains the Redis configuration files
- `/environment-config/roles/redis.yaml` - Contains the Kubernetes RBAC roles for Redis
- `/environment-config/secrets/redis.yaml` - Contains the Kubernetes secrets for Redis
- `/environment-config/namespace.yaml` - Contains the Kubernetes namespace configuration for Redis

## Functionality

- **High Availability**: The Redis Sentinel setup ensures that if the master node fails, one of the replicas will be
  promoted to master, maintaining availability.
- **Automatic Failover**: Redis Sentinel automatically detects failures and promotes replicas to master without manual
  intervention.
- **Monitoring**: Redis Sentinel continuously monitors the health of the Redis instances and provides notifications in
  case of failures.
- **Automatic Configuration**: The deployment includes configurations to handle edge cases, ensuring a smooth and
  reliable deployment process.

## Usage

To deploy Redis Sentinel in your Kubernetes cluster, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:pingmyheart/K8s-Redis-Sentinel.git
   ```
2. Apply Kubernetes configurations:
   ```bash
   kubectl apply -f environment-config/namespace.yaml
   kubectl apply -f environment-config/roles/redis.yaml
   kubectl apply -f environment-config/secrets/redis.yaml
   kubectl apply -f environment-config/config/redis.yaml
   kubectl apply -f app/redis/service/service.yaml
   kubectl apply -f app/redis/deploy/deployment.yaml
   ```