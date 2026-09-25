---
type: machine
title: CarpeDiem
platform: htb
os: linux
difficulty: hard
tags: [docker, web, ssh, pivoting, encryption, voip, rce, privesc, container-escape]
solved: 2026-07-09
sources: [[htb-carpediem]]
related: []
---
# CarpeDiem
> CarpeDiem is a hard Linux box involving Docker container exploitation. The attack path includes web application exploitation for initial access, network pivoting through multiple containers, voicemail credential harvesting, TLS decryption with weak ciphers, CMS exploitation via malicious plugin upload, cron job abuse for container root, and Docker escape via cgroups (CVE-2022-0492).

## Attack path
1. [[web-enumeration]] → Admin access via login_type parameter tampering
2. [[file-upload]] → Webshell upload → Container foothold
3. [[network-pivoting]] → [[chisel]] tunnel to internal services
4. [[ticket-system]] → Voicemail credentials for new user
5. [[ssh-access]] as hflaccus
6. [[network-sniffing]] → Weak TLS cipher → [[tls-decryption]] with private key
7. [[cms-exploitation]] → Malicious plugin upload → [[container-privilege-escalation]]
8. [[docker-escape]] via cgroups → [[host-privilege-escalation]]

## Techniques used
- [[parameter-tampering]] — Modify login_type to gain admin access
- [[file-upload]] — Upload PHP webshell via quarterly report form
- [[network-pivoting]] — Chisel SOCKS proxy through Docker network
- [[voip-credential-harvesting]] — Access voicemail to get user credentials
- [[tls-decryption]] — Decrypt TLS traffic with weak RSA cipher and private key
- [[plugin-upload]] — Upload malicious Backdrop CMS plugin for RCE
- [[cron-job-abuse]] — Modify index.php executed by root cron
- [[docker-escape]] — CVE-2022-0492 cgroups release_agent exploit

## Tools used
- [[nmap]] — Port scanning and service detection
- [[feroxbuster]] — Directory brute force
- wfuzz — Subdomain and ticket ID fuzzing
- [[chisel]] — SOCKS proxy for network tunneling
- [[tcpdump]] — Network traffic capture
- Wireshark — PCAP analysis and TLS decryption
- Zoiper — VoIP softphone for voicemail access
- [[python]] — Webshell and exploit scripts
- [[curl]] — HTTP requests and webshell execution
- [[ssh]] — Remote shell access
- nc — Reverse shell connections

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 8.2p1)
- 80/tcp — [[http]] (nginx)
- 443/tcp — [[https]] (Backdrop CMS)
- 3306/tcp — MySQL
- 27017/tcp — MongoDB
- 8118/tcp — Trudesk application

## Lessons / notes
- Docker container networks often contain additional services not exposed externally
- Weak TLS ciphers (RSA without PFS) allow decryption with private key
- Private keys for TLS often stored in /etc/ssl/certs with certificates
- VoIP systems may contain credential delivery mechanisms
- CMS plugin upload functionality is common RCE vector
- Cron jobs running as root can be exploited via writable script files
- CVE-2022-0492 allows container escape through cgroups release_agent
