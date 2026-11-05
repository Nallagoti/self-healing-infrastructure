# Testing Report

## 1. Objective

To verify website monitoring, failure detection, automatic NGINX recovery, and email notifications.

## 2. Test Cases and Results

| Test Case | Expected Result | Actual Result |
|---|---|---|
| NGINX website check | Website responds successfully | Passed |
| Prometheus monitoring | Metrics are collected | Passed |
| Blackbox health check | Website availability is detected | Passed |
| NGINX failure simulation | Downtime alert is generated | Passed |
| Webhook execution | Recovery automation is triggered | Passed |
| Ansible recovery | NGINX starts automatically | Passed |
| Recovery email | Gmail receives recovery notification | Passed |

## 3. Final Result

NGINX was successfully recovered automatically after stopping the service. The webhook triggered the Ansible playbook, and a recovery notification was received through Gmail.

## 4. Conclusion

The testing confirmed that the self-healing infrastructure workflow works successfully for the tested NGINX failure and recovery scenario.
