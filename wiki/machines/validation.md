---
type: machine
title: Validation
platform: htb
os: linux
difficulty: easy
tags: [web, sqli, file-write, password-reuse]
solved: 2026-07-09
sources: [[htb-validation]]
related: []
---
# Validation
> UHC qualifier box featuring a registration site with second-order SQL injection in the country field, allowing extraction of the FILE privilege to write a PHP webshell, with simple password reuse for root access.

## Attack path
1. [[second-order-sqli]] — Inject UNION via country parameter in registration to enumerate database
2. [[sqli-file-write]] — Use FILE privilege to write PHP webshell to webroot
3. [[password-reuse]] — Reuse database password for root login via `su`

## Techniques used
- [[second-order-sqli]] — Registration form stores country in database, later retrieved on profile page allowing UNION injection
- [[sqli-file-write]] — SQL FILE privilege used to write webshell via `SELECT ... INTO OUTFILE`
- [[password-reuse]] — Database credentials (`uhc:uhc-9qual-global-pw`) work for root

## Tools used
- [[nmap]]
- [[feroxbuster]]
- [[netcat]]
- Python (custom SQLi shell)
- [[curl]]

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 80/tcp — [[http]] — Apache httpd 2.4.48 (Debian)
- 4566/tcp — [[http]] — nginx (localstack)
- 8080/tcp — [[http]] — nginx (bad gateway)

## Lessons / notes
- Second-order SQLi: input stored in database, later retrieved in different query allowing injection
- Cookie was MD5 hash of username (predictable, but not exploitable)
- Box ran in Docker container (evidenced by `.dockerenv` file and `172.18.0.0/16` IP)
- MySQL user had extensive privileges including FILE
- Simple credential reuse from database config to root
