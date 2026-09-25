---
type: machine
title: Mischief
platform: htb
os: linux
difficulty: insane
tags: [linux, ipv6, snmp, command-injection, acl]
solved: 2026-07-09
sources: [[htb-mischief]]
related: []
---
# Mischief

> Mischief is an Insane-level Linux box that heavily features IPv6 enumeration, SNMP credential harvesting, and command injection with output filtering, culminating in exploiting file access control lists to restrict su binary usage.

## Attack path
1. Use [[snmp]] enumeration to discover IPv6 address and webserver credentials from process list
2. Access IPv6-only command execution panel using harvested credentials and hydra brute force
3. Achieve [[command-injection]] using command chaining to bypass output filtering
4. Obtain www-data shell via Python reverse shell over IPv6
5. Recover loki credentials from filesystem and use sudo/systemd-run for root access
6. Exploit [[acl]] misconfiguration to prevent loki from using su while www-data can

## Techniques used
- [[snmp]]-enumeration — Walk SNMP MIB trees to discover IPv6 addresses, process credentials, and network configuration
- [[ipv6-enumeration]] — Discover IPv6-only webserver not visible on standard IPv4 scans
- [[credential-harvesting]] — Extract cleartext passwords from SNMP process command-line arguments
- [[command-injection]] — Inject arbitrary commands into web interface that filters output
- [[command-chaining]] — Bypass command execution filtering by chaining with semicolons
- [[ipv6-reverse-shell]] — Create Python reverse shell that connects over IPv6 instead of IPv4
- [[sudo-abuse]] — Exploit NOPASSWD: ALL configuration for privilege escalation
- [[acl]] — Identify and understand File Access Control Lists restricting binary execution

## Tools used
- [[nmap]] — TCP and UDP port scanning with IPv6 support
- [[snmpwalk]] — SNMP MIB enumeration and credential discovery
- [[feroxbuster]] — Directory brute force on web services
- [[hydra]] — Web form brute force against login page
- [[python]] — Reverse shell creation and command execution
- [[netcat]] — IPv6 listener for reverse shell connections
- [[getfacl]] — Display file access control lists to understand permission restrictions

## Services / ports
- [[ssh]] (22) — Secure shell access
- [[http]] (80, 3366) — IPv4 and IPv6 web servers
- [[snmp]] (161) — SNMP agent with public community string
- [[dns]] (53) — DNS service on localhost

## Lessons / notes
- IPv6 addresses can be discovered through SNMP even when not visible in standard nmap scans
- SNMP often exposes sensitive information including process command-line arguments with credentials
- Command injection interfaces that filter output can often be bypassed using command chaining
- File Access Control Lists (ACLs) provide more granular permission control than traditional Unix permissions
- IoT and embedded devices may have non-standard services on unexpected ports
- IPv6 link-local addresses (fe80::/10) are automatically configured and may expose additional services
- Defensive WAFs/command filters should account for command chaining techniques
- Always check both IPv4 and IPv6 when enumerating targets

## Beyond root
- Command injection can be achieved without valid credentials by discovering the POST parameter directly
- Data can be exfiltrated through ICMP ping packets by encoding data in ping payloads
- IPv6 firewall rules may differ significantly from IPv4 rules, creating attack opportunities
