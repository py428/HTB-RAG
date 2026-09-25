---
type: machine
title: Eureka
platform: htb
os: linux
difficulty: hard
tags: [linux, spring-boot, web, ad]
solved: 2026-07-09
sources: [[htb-eureka]]
related: []
---
# Eureka
> Linux Spring Boot microservices box featuring exposed heapdump endpoint for credential extraction, Eureka service discovery hijacking to intercept user credentials, and Bash arithmetic injection in log analysis script for root privilege escalation.

## Attack path
1. [[heapdump-analysis]] of exposed Spring Boot actuator endpoint extracts database credentials
2. SSH access with extracted credentials (oscar190)
3. [[service-hijacking]] — Register malicious USER-MANAGEMENT-SERVICE in Eureka to intercept login
4. [[log-poisoning]] — Exploit Bash arithmetic injection in log_analyse.sh via writable log directory
5. SetUID binary creation for root access

## Techniques used
- [[heapdump-analysis]] — Downloading and analyzing Java heap dump with VisualVM/JDumpSpider to extract credentials
- [[service-hijacking]] — Registering rogue service in Eureka discovery server to intercept traffic
- [[log-poisoning]] — Injecting malicious entries into log files processed by privileged scripts
- [[bash-arithmetic-injection]] — Exploiting Bash -eq operator in arithmetic comparisons for command execution
- [[setuid-binary]] — Creating SetUID copy of bash for persistence

## Tools used
- [[nmap]], [[feroxbuster]], JDumpSpider, VisualVM, [[curl]], [[netexec]]

## Services / ports
- [[ssh]] (22), [[http]] (80/8761)

## Lessons / notes
- Spring Boot actuator endpoints (especially /actuator/heapdump) can expose sensitive credentials
- JDumpSpider automates extraction of interesting data from Java heap dumps
- Eureka service discovery allows rogue service registration to intercept internal traffic
- Bash arithmetic comparisons with -eq operator can be exploited for command injection via array syntax
- Log directories writable by low-priv users can be poisoned to inject into privileged scripts
- Microservices architecture increases attack surface through service-to-service communication
