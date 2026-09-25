---
type: source
title: "HTB Eureka writeup"
raw: raw/htb-eureka.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[eureka]]
---
# Source: HTB Eureka writeup

> In-depth analysis of Eureka Linux Spring Boot box covering heapdump analysis for credential extraction, Eureka service hijacking for credential interception, and Bash arithmetic injection in log analysis scripts.

## Key facts extracted
- Spring Boot application with exposed /actuator/heapdump endpoint (76 MB)
- JDumpSpider extracts: oscar190 / 0sc@r190_S0l!dP@sswd, EurekaSrvr / 0scarPWDisTheB3st
- Four Spring microservices: Furni (8082), user-management-service (8081), cloud-gateway (8080), Eureka-Server (8761)
- miranda-wise@furni.htb logs in every 2 minutes via automated script
- /opt/log_analyse.sh runs as root processing cloud-gateway logs
- Bash arithmetic injection in analyze_http_statuses function via STATUS_CODES array
- Log directory (/var/www/web/*/log/) writable by developers group

## Filed into
[[eureka]], [[heapdump-analysis]], [[service-hijacking]], [[log-poisoning]], [[bash-arithmetic-injection]]
