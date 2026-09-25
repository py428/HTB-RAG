---
type: machine
title: CozyHosting
platform: htb
os: linux
difficulty: easy
tags: [web, linux, privesc, spring-boot, actuator, postgresql, command-injection, sudo-abuse]
solved: 2026-07-09
sources: [[htb-cozyhosting]]
related: []
---
# CozyHosting
> Java Spring Boot web hosting company with exposed actuator endpoints leading to session hijacking, command injection in admin panel, PostgreSQL database access for credential cracking, and sudo ProxyCommand abuse for root access.
## Attack path
1. [[spring-boot-actuator]] — enumerate exposed actuator endpoints, leak active session IDs
2. [[session-hijacking]] — steal authenticated user session via `/actuator/sessions`
3. [[command-injection]] — bypass input filters in SSH execution feature using `${IFS}` and brace expansion
4. [[postgresql-access]] — extract database credentials from JAR file, dump user hashes
5. [[password-cracking]] — crack bcrypt hashes to get user password
6. [[sudo-proxycommand]] — abuse `sudo ssh` with ProxyCommand to execute as root
## Techniques used
- [[spring-boot-actuator]] — exposed `/actuator/sessions` endpoint leaked active session IDs
- [[session-hijacking]] — stole `kanderson` session cookie to bypass authentication
- [[command-injection]] — bypassed filters in `/executessh` using `${IFS}` for whitespace and `#` for comments
- [[jar-analysis]] — extracted PostgreSQL credentials from `cloudhosting-0.0.1.jar`
- [[postgresql-access]] — connected to database, dumped admin bcrypt hash
- [[password-cracking]] — cracked bcrypt hash with hashcat to get `manchesterunited` password
- [[sudo-proxycommand]] — used `sudo ssh -o ProxyCommand` for root shell via GTFObins
## Tools used
- [[nmap]], [[feroxbuster]], [[curl]], [[hashcat]], [[ssh]], netcat, python
## Services / ports
- SSH (22), [[http]] (80)
## Lessons / notes
- Spring Boot actuators can leak sensitive session data if exposed
- Command injection filters can often be bypassed with variable substitution
- Database credentials in configuration files may be reused for user access
- Sudo permissions on SSH can be abused through ProxyCommand for privilege escalation