---
type: machine
title: Monitored
platform: htb
os: linux
difficulty: medium
tags: [nagios, snmp, ldap, api, sqli, privesc, sudo]
solved: 2026-07-09
sources: [[htb-monitored]]
related: []
---
# Monitored

> Nagios XI monitoring server with multiple privilege escalation paths via SNMP enumeration, SQL injection, API abuse, and sudo misconfigurations.

## Attack path

1. [[snmp-enum]] — enumerate running processes and find `sudo` command with credentials
2. [[api-abuse]] — authenticate to Nagios API using disabled account credentials
3. [[sql-injection]] — exploit CVE-2023-40931 in banner message endpoint to leak admin API key
4. [[api-abuse]] — create new admin user via API with `auth_level=admin`
5. [[rce]] — create custom Nagios command with reverse shell payload
6. [[privesc]] — overwrite Nagios binary and restart service OR [[symlink-abuse]] with `getprofile.sh` to leak root SSH key

## Techniques used

- [[snmp-enum]] — SNMP `snmpwalk` to enumerate processes and find credentials in command line arguments
- [[api-abuse]] — Nagios XI API token-based authentication and user creation
- [[sql-injection]] — CVE-2023-40931 in `banner_message-ajaxhelper.php` for blind SQL injection
- [[rce]] — Nagios Core Config Manager command execution feature
- [[symlink-abuse]] — Replace writable log file with symlink to sensitive file (root SSH key)
- [[sudo-abuse]] — Overwrite service binary and restart via `manage_services.sh`

## Tools used

- [[nmap]], [[snmpwalk]], [[sqlmap]], [[curl]], [[netexec]]

## Services / ports

- 22/tcp — [[ssh]] — OpenSSH 8.4
- 80/tcp — [[http]] — Apache 2.4.56 (redirects to https://nagios.monitored.htb/)
- 389/tcp — [[ldap]] — OpenLDAP
- 443/tcp — [[https]] — Apache 2.4.56 (Nagios XI)
- 161/udp — [[snmp]] — NET-SNMP
- 5667/tcp — tcpwrapped

## Lessons / notes

- Nagios XI API authentication works with both disabled accounts and full admin accounts
- SQLMap boolean-based blind injection much faster than time-based for this vulnerability
- Multiple sudo paths: service binary replacement or symlink attacks on log collection scripts
- `getprofile.sh` script tail's various log files including writable `phpmailer.log`
- Nagios service binary owned by `nagios` user, allowing replacement and privilege escalation on restart
