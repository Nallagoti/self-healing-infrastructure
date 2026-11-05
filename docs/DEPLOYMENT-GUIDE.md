# Deployment Guide

## 1. Infrastructure Setup

- Created an Ubuntu EC2 instance on AWS.
- Connected to the instance using SSH.
- Updated Ubuntu packages.

## 2. NGINX Setup

- Installed NGINX web server.
- Configured an HTTPS website.
- Created a health-check endpoint.
- Configured Basic Authentication for the monitoring dashboard.

## 3. Monitoring Setup

- Installed Prometheus.
- Installed Blackbox Exporter.
- Configured Prometheus to monitor the NGINX health endpoint.
- Created alert rules to detect website downtime.

## 4. Alertmanager Setup

- Installed and configured Alertmanager.
- Connected Alertmanager to Prometheus.
- Configured Gmail SMTP for email notifications.
- Configured the Python webhook receiver.

## 5. Self-Healing Automation

- Created a Python webhook to receive alerts.
- Created an Ansible playbook to recover NGINX.
- Configured a systemd service to run the webhook.
- Configured permissions for automated recovery.

## 6. Verification

- Verified NGINX website availability.
- Verified Prometheus and Blackbox monitoring.
- Stopped NGINX to simulate a failure.
- Verified automatic recovery through Ansible.
- Verified the recovery email notification in Gmail.
