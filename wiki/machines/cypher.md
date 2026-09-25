---
type: machine
title: Cypher
platform: htb
os: linux
difficulty: medium
tags: [linux, web, ad, privesc, docker, sudo, neo4j, cypher]
solved: 2026-07-09
sources: [[htb-cypher]]
related: []
---
# Cypher

> Graph database-focused Linux box with a Neo4J web application vulnerable to Cypher injection, leading to command execution via a custom extension, then password reuse and sudo abuse of the bbot tool for root.

## Attack path

1. [[nmap]] port scan → [[ssh]] and [[http]]
2. [[feroxbuster]] directory enumeration → discover testing directory with JAR file
3. [[jadx-gui]] reverse engineering → find command injection in custom Neo4j extension
4. [[cypher-injection]] to bypass authentication and access the dashboard
5. [[command-injection]] via vulnerable `custom.getUrlStatusCode` function → shell as neo4j
6. Password in [[bash-history]] → shell as graphasm
7. [[sudo]] privilege escalation → [[bbot]] module injection → root shell

## Techniques used

- [[cypher-injection]] — Bypass login on Neo4J graph database web application using UNION-based injection to return controlled hash
- [[command-injection]] — Inject commands via custom Neo4j APOC extension function `custom.getUrlStatusCode` that executes curl commands
- [[password-reuse]] — Neo4j database password found in `.bash_history` is reused by the graphasm user
- [[sudo-abuse]] — Run bbot tool as root to load custom modules and execute arbitrary code as SYSTEM

## Tools used

- [[nmap]] — Port scanning and service detection
- [[feroxbuster]] — Directory brute forcing to discover `/testing` directory with JAR file
- [[jadx-gui]] — Reverse engineering Java JAR file to find command injection vulnerability
- [[curl]] — Command execution and testing during exploitation
- [[netcat]] — Reverse shell listener and establishing connections
- [[bbot]] — OSINT tool with module loading feature exploited for privilege escalation

## Services / ports

- 22/tcp [[ssh]] — OpenSSH 9.6p1 Ubuntu
- 80/tcp [[http]] — nginx 1.24.0 Ubuntu hosting Neo4J graph database application

## Lessons / notes

- Neo4J Cypher injection requires understanding the graph query language syntax and how to manipulate UNION queries to control the output
- Custom database extensions can introduce command injection vulnerabilities even when the main application is secure
- The bbot tool's module loading functionality can be abused to execute arbitrary Python code when run with sudo privileges
- Always check for passwords in `.bash_history` files on Linux systems, especially for service accounts like neo4j
- Graph databases like Neo4J have unique injection points compared to traditional SQL databases
- Docker containers often have weaker isolation than VMs, making host filesystem access easier