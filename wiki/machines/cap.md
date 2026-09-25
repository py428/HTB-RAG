---
type: machine
title: Cap
platform: htb
os: linux
difficulty: easy
tags: [idor, pcap, linux, ftp, ssh, web, privesc, capabilities]
solved: 2026-07-09
sources: [[htb-cap]]
related: []
---
# Cap
> Cap is an easy Linux box featuring a web application with IDOR vulnerability to access PCAP files. The initial foothold involves finding FTP credentials in a PCAP file, which also provide SSH access. Privilege escalation abuses Linux capabilities, specifically cap_setuid on Python, to gain root shell.

## Attack path
1. [[web-enumeration]] → IDOR vulnerability in PCAP download → [[idor]]
2. [[pcap-analysis]] → FTP credentials extraction
3. [[ftp-access]] → [[ssh-access]] with same credentials
4. [[linux-capabilities]] → cap_setuid on Python → [[privilege-escalation]]

## Techniques used
- [[idor]] — Sequential PCAP IDs allow downloading other users' captures
- [[pcap-analysis]] — Extract FTP credentials from packet capture
- [[linux-capabilities]] — Python with cap_setuid capability for root shell

## Tools used
- [[nmap]] — Port scanning and service detection
- [[feroxbuster]] — Directory brute force
- wget — Download PCAP files via loop
- [[smbclient]] — FTP access and file operations
- [[ssh]] — Remote shell access
- python3 — Capability abuse for privilege escalation

## Services / ports
- 21/tcp — [[ftp]] (vsftpd 3.0.3)
- 22/tcp — [[ssh]] (OpenSSH 8.2p1)
- 80/tcp — [[http]] (Python Flask)

## Lessons / notes
- IDOR vulnerabilities often involve predictable sequential IDs
- FTP and SSH frequently share credentials
- Linux capabilities can provide root-like access without full privileges
- Python cap_setuid allows arbitrary UID changes for privilege escalation
