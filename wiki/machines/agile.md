---
type: machine
title: Agile
platform: htb
os: linux
difficulty: medium
tags: [web, linux, privesc, flask, debug, sudo]
solved: 2026-07-09
sources: [[htb-agile]]
related: []
---
# Agile
> A password manager web application with Flask debug mode, file read vulnerability leading to initial shell, Chrome debug exploitation for user pivot, and sudo CVE-2023-22809 for root access.

## Attack path
1. [[directory-traversal]] in export feature to read arbitrary files
2. [[flask-debug-rce]] by calculating PIN from leaked system information
3. [[database-credential-exposure]] to obtain user password from MySQL database
4. [[chrome-debug-exploitation]] of Selenium testing instance for session hijacking
5. [[sudo-cve-2023-22809]] to edit virtual environment activation script for root shell

## Techniques used
- [[directory-traversal]] — File read vulnerability in /vault/export endpoint
- [[flask-debug-rce]] — PIN generation from /proc/self/environ, MAC address, machine-id, cgroup
- [[database-credential-exposure]] — MySQL credentials stored in config_prod.json
- [[chrome-debug-exploitation]] — Remote debugging port 41829 exposed in Selenium tests
- [[sudo-cve-2023-22809]] — Sudoedit vulnerability allowing arbitrary file writes

## Tools used
[[nmap]] [[feroxbuster]] mysql chrome python3

## Services / ports
- [[ssh]] 22 — OpenSSH 8.9p1 Ubuntu 3ubuntu0.1
- [[http]] 80 — nginx 1.18.0 (Ubuntu) hosting Flask application
- Chrome Debug 41829 — Selenium remote debugging port
- MySQL 3306 — localhost only

## Lessons / notes
- Flask debug mode requires PIN calculation using multiple system-specific pieces of information
- The wsgi_app module name (not Flask) is required for correct PIN generation on Gunicorn
- Chrome remote debugging allows complete session hijacking including cookies and localStorage
- Sudo CVE-2023-22809 allows editing arbitrary files via sudoedit when certain permissions exist
- All users on the system source the application virtual environment, making it a privilege escalation target

## CVEs
- CVE-2023-22809
