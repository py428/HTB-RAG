---
type: machine
title: MonitorsTwo
platform: htb
os: linux
difficulty: easy
tags: [cacti, rce, docker, privesc, setuid]
solved: 2026-07-09
sources: [[htb-monitorstwo]]
related: []
---
# MonitorsTwo

> Updated Cacti exploitation with command injection vulnerability, followed by Docker privilege escalation via SetUID binary creation.

## Attack path

1. [[rce]] — exploit CVE-2022-46169 in Cacti `remote_agent.php` (command injection)
2. [[container-enumeration]] — identify Docker container environment
3. [[database-access]] — connect to MySQL database from container
4. [[hash-cracking]] — dump and crack marcus password hash using john
5. [[ssh]] — authenticate as marcus over SSH with cracked credentials
6. [[docker-privesc]] — exploit CVE-2021-41091/CVE-2021-41103 (Docker SetUID binary)
7. [[setuid-abuse]] — create SetUID bash binary in container and execute from host

## Techniques used

- [[rce]] — CVE-2022-46169: Unauthenticated command injection in `poller_id` parameter with X-Forwarded-For bypass
- [[hash-cracking]] — John the Ripper to crack bcrypt hash from Cacti database
- [[docker-privesc]] — CVE-2021-41091: Docker data directory permissions allow executing SetUID binaries
- [[setuid-abuse]] — Create SetUID copy of bash in container, execute from host for root shell

## Tools used

- [[nmap]], [[wfuzz]], [[curl]], [[john]], [[ssh]], [[netcat]]

## Services / ports

- 22/tcp — [[ssh]] — OpenSSH 8.2
- 80/tcp — [[http]] — nginx 1.18.0 (Cacti 1.2.22)

## Lessons / notes

- CVE-2022-46169 bypasses auth check via X-Forwarded-For: 127.0.0.1 header
- Brute forcing `host_id` and `local_data_ids[]` required to find valid graph targets
- Docker 20.10.5 vulnerable to CVE-2021-41091 (container SetUID binary execution)
- `/var/lib/docker/overlay2/*/merged/` paths allow executing container binaries from host
- SetUID bash with `-p` flag preserves root privileges when executed
