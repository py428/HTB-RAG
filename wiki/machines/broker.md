---
type: machine
title: Broker
platform: htb
os: linux
difficulty: easy
tags: [linux, web, privesc]
solved: 2026-07-09
sources: [[htb-broker]]
related: []
---
# Broker
> Easy Linux box featuring unauthenticated ActiveMQ RCE via CVE-2023-46604, followed by nginx abuse for file read/write and alternative LD_PRELOAD privilege escalation.
## Attack path
1. [[activemq-rce]] — Exploit CVE-2023-46604 deserialization vulnerability for initial shell
2. [[nginx-file-read]] — Abuse sudo nginx to create malicious server reading files as root
3. [[nginx-file-write]] — Use nginx PUT method to write SSH key for root access
4. [[ld-so-preload]] — Alternative escalation via nginx error log poisoning and shared library
## Techniques used
- [[activemq-rce]] — Spring XML deserialization chain in ActiveMQ 5.15.15 (CVE-2023-46604)
- [[nginx-file-read]] — Sudo nginx configuration to serve filesystem as root
- [[nginx-file-write]] — nginx DAV PUT method for file creation as root
- [[ld-so-preload]] — Poison /etc/ld.so.preload via nginx error_log for privilege escalation
## Tools used
- [[nmap]] — Port scan identifying ActiveMQ and nginx
- python — CVE-2023-46604 exploit (evkl1d POC)
- [[curl]] — HTTP interaction and nginx testing
- [[nginx]] — File read/write abuse with custom configurations
- gcc — Compile malicious shared library for LD_PRELOAD
## Services / ports
- [[ssh]] (22) — OpenSSH 8.9p1 Ubuntu 3ubuntu0.4
- [[http]] (80) — nginx 1.18.0 with basic auth
- mqtt (1883) — MQTT protocol for ActiveMQ
- amqp (5672) — AMQP protocol for ActiveMQ
- ActiveMQ (61616) — OpenWire transport for RCE exploitation
- Jetty (8161/61614) — ActiveMQ web interface
## Lessons / notes
- ActiveMQ CVE-2023-46604 is a critical unauthenticated RCE with CVSS 10.0
- Spring framework deserialization chains provide powerful gadget chains
- Sudo nginx permissions provide excellent file read/write capabilities
- LD_PRELOAD poisoning is a reliable technique when you can write to system files
- Multiple privilege escalation paths exist when you have sudo nginx access