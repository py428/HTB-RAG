---
type: source
title: "HTB CozyHosting writeup"
raw: raw/htb-cozyhosting.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[cozyhosting]]
---
# Source: HTB CozyHosting writeup
> Web hosting company running Java Spring Boot with exposed actuator endpoints allowing session hijacking. Command injection in admin panel leads to initial access. PostgreSQL credentials from JAR file enable password cracking for user access. Sudo SSH abuse with ProxyCommand leads to root shell.
## Key facts extracted
- Spring Boot Actuator exposed at `/actuator/sessions` leaking active user sessions
- Admin panel at `/admin` with SSH execution feature vulnerable to command injection
- Input filtering bypassed using `${IFS}` for whitespace and brace expansion
- PostgreSQL database credentials stored in `cloudhosting-0.0.1.jar`
- Admin password `manchesterunited` cracked from bcrypt hash
- User `josh` can run `ssh` as root via sudo
## Filed into
[[cozyhosting]], [[spring-boot-actuator]], [[session-hijacking]], [[command-injection]], [[postgresql-access]], [[password-cracking]], [[sudo-proxycommand]]