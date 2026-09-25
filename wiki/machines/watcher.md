---
type: machine
title: Watcher
platform: htb
os: linux
difficulty: medium
tags: [linux, web, cve, sqli, ci-cd, ssh-tunneling, credential-harvesting]
solved: 2026-07-09
sources: [[htb-watcher]]
related: []
---
# Watcher
> Watcher is a medium Linux box featuring a Zabbix monitoring server and TeamCity CI/CD platform. Initial access exploits CVE-2024-22120, a blind SQL injection in Zabbix audit logs, to leak admin session credentials and achieve RCE. Lateral movement involves poisoning the Zabbix login page to harvest Frank's credentials, which also work for TeamCity. Root access is achieved through TeamCity build pipeline command execution running as root.

## Attack path
1. [[subdomain-enumeration]] via ffuf → discover zabbix.watcher.vl
2. [[cve-2024-22120]] (Zabbix blind SQLi) → leak admin session, get RCE as zabbix
3. [[ssh-tunneling]] to access localhost TeamCity on port 8111
4. [[source-code-modification]] of Zabbix index.php → harvest Frank's credentials
5. [[ci-cd-build-exploitation]] in TeamCity → root shell via build step execution

## Techniques used
- [[blind-sql-injection]] — Zabbix audit log parameter vulnerable to time-based SQL injection in clientip field
- [[session-hijacking]] — Extracted admin session ID and signing key via SQL injection to bypass authentication
- [[ssh-tunneling]] — Created SSH tunnel through zabbix user to access localhost-only TeamCity instance
- [[credential-harvesting]] — Modified Zabbix login PHP source to capture user credentials to file
- [[ci-cd-build-exploitation]] — Created malicious build step in TeamCity with reverse shell executing as root

## Tools used
- [[nmap]], [[ffuf]], [[feroxbuster]], [[curl]], [[mysql]], [[ssh]], [[netcat]], [[python]]

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 8.9)
- 80/tcp — [[http]] (Apache 2.4.52) → Zabbix frontend, Watcher landing page
- 10050/tcp — zabbix-agent
- 10051/tcp — zabbix-trapper
- 8111/tcp — TeamCity (localhost only)

## Lessons / notes
- Zabbix guest access still provides session ID for SQL injection exploitation
- TeamCity running on localhost only requires SSH tunneling for external access
- CI/CD build pipelines often run with elevated privileges making them valuable targets
- Modifying login page source code can be effective for credential harvesting
- Shared credentials across services (Zabbix to TeamCity) common in real environments
- Time-based blind SQL injection can be slow but reliable for data extraction
