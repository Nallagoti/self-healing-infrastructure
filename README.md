# Self-Healing Infrastructure with Monitoring and Email Alerts

## Project Overview

This project implements a self-healing infrastructure system that monitors an NGINX website using Prometheus and Blackbox Exporter.

When the website goes down, Prometheus detects the failure and sends an alert to Alertmanager. Alertmanager sends an email notification and triggers a Python webhook.

The webhook executes an Ansible playbook to automatically recover the NGINX service.

When the website recovers, Alertmanager sends a recovery notification to Gmail.

## Technologies Used

- AWS EC2
- Ubuntu Linux
- NGINX
- Prometheus
- Blackbox Exporter
- Alertmanager
- Ansible
- Python
- Gmail SMTP
- HTTPS / SSL
- Git and GitHub

## Project Features

- HTTPS-enabled NGINX website
- Password-protected dashboard
- Website health monitoring
- Prometheus metrics collection
- Blackbox HTTP monitoring
- Automatic NGINX recovery using Ansible
- Gmail email notifications
- Prometheus and Alertmanager dashboards

## Architecture

See [Architecture Diagram](docs/architecture.md).

## Project Testing

1. Verified the NGINX website over HTTPS.
2. Verified Prometheus and Blackbox Exporter.
3. Stopped the NGINX service for testing.
4. Prometheus detected the website failure.
5. Alertmanager triggered the recovery webhook.
6. Ansible automatically started NGINX.
7. Verified that NGINX recovered successfully.
8. Received a Gmail recovery notification.

## Project Structure

```text
self-healing-infrastructure/
├── README.md
├── .gitignore
├── nginx/
├── prometheus/
├── blackbox/
├── alertmanager/
├── ansible/
├── webhook/
├── systemd/
├── docs/
└── screenshots/
```

## Security

- No passwords or tokens are included.
- Credentials must be configured securely during deployment.
- Private keys and sensitive files must not be uploaded to GitHub.

## Author

Nissitha Nallagoti

DevOps Engineer | Fresher
