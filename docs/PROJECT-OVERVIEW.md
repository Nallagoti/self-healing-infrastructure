# Project Overview

## 1. Introduction

Self-Healing Infrastructure is a DevOps project that monitors an NGINX website and automatically recovers it when it goes down.

## 2. Objective

The main objective is to reduce manual intervention and improve application availability using monitoring and automation tools.

## 3. Tools and Technologies

- AWS EC2 – Cloud infrastructure
- Ubuntu – Operating system
- NGINX – Web server
- Prometheus – Monitoring and alerting
- Blackbox Exporter – Website availability checks
- Alertmanager – Alert management and notifications
- Python – Webhook automation
- Ansible – Automatic NGINX recovery
- Gmail SMTP – Email notifications

## 4. Working Process

1. Blackbox Exporter checks the NGINX website.
2. Prometheus collects monitoring metrics.
3. If NGINX goes down, Prometheus generates an alert.
4. Alertmanager sends an alert notification and triggers the Python webhook.
5. Python webhook executes the Ansible playbook.
6. Ansible ensures that NGINX is running.
7. Prometheus detects recovery.
8. Alertmanager sends a recovery email to Gmail.

## 5. Expected Outcome

The system detects website failures, automatically recovers the NGINX service, and sends email notifications about the failure and recovery.