---
type: machine
title: Doctor
platform: htb
os: linux
difficulty: easy
tags: [linux, web, ssti, command-injection, splunk, log-analysis]
solved: 2026-07-09
sources: [[htb-doctor]]
related: []
---
# Doctor
> Healthcare messaging platform with two initial access vectors: server-side template injection in archive feed or command injection via URL validation curl. Password reuse between web application and Splunk enables privilege escalation using SplunkWhisperer2 exploit.

## Attack path
1. [[ssti]] — Inject Jinja2 template in message title that executes in /archive RSS feed
2. [[command-injection]] — Alternative: Inject commands via URL validation using curl
3. [[log-analysis]] — Find password in Apache backup logs from failed reset attempt
4. [[splunk-rce]] — Exploit Splunk with SplunkWhisperer2 for root shell

## Techniques used
- [[ssti]] — Jinja2 template injection in message title renders in /archive RSS XML output
- [[command-injection]] — URL validation uses os.system(curl) without sanitization enabling shell injection
- [[log-analysis]] — Apache backup logs contain password "Guitar123" from failed reset
- [[password-reuse]] — Credentials shared between web application and Splunk service
- [[splunk-rce]] — SplunkWhisperer2 exploits Splunk universal forwarder for RCE

## Tools used
[[nmap]], [[curl]], [[netcat]], [[linpeas]], [[ssh]], [[python]], [[tcpdump]]

## Services / ports
- [[ssh]] (22) — OpenSSH 8.2p1 Ubuntu
- [[http]] (80) — Apache 2.4.41 / Werkzeug Python
- Splunk (8089) — Splunkd management interface

## Lessons / notes
- SSTI testing requires checking both page rendering and alternate output formats like RSS feeds
- Command injection in URL validation often uses curl or similar tools without proper sanitization
- Log files often contain passwords from failed operations or reset attempts
- Splunk management interface provides powerful attack surface when credentials are known
- Flask cookies use signed serialization that can preserve sessions across database resets
- Membership in adm group provides access to valuable log files for privilege escalation
