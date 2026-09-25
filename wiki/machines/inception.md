---
type: machine
title: Inception
platform: htb
os: linux
difficulty: medium
tags: [linux, web, php, lfi, webdav, forward-shell, sudo, ftp, tftp, cron]
solved: 2026-07-09
sources: [[htb-inception]]
related: []
---
# Inception
> Inception is one of the first HTB boxes to use containers. The attack path involves exploiting dompdf LFI vulnerability, WebDAV for webshell upload, forward shell techniques due to blocked outbound traffic, sudo for container root, then abusing FTP and TFTP access from container to write cron pre-invoke scripts on the host system.

## Attack path
1. [[lfi]] — Exploit dompdf 0.6.0 LFI via php://filter to read configuration files
2. [[webdav]] — Upload PHP webshell via WebDAV using credentials from config
3. [[forward-shell]] — Create custom Python forward shell due to blocked outbound traffic
4. [[sudo]] — Use sudo access in container to get root
5. [[tunnel]] — Pivot from container to host via FTP and TFTP access
6. [[cron-hijack]] — Write apt pre-invoke script via TFTP to establish reverse shell

## Techniques used
- [[lfi]] — Local file inclusion in dompdf using php://filter for base64-encoded file reads
- [[webdav]] — WebDAV file upload for PHP webshell using davtool and curl
- [[forward-shell]] — Custom Python forward shell when outbound traffic is blocked
- [[sudo]] — Full sudo access in container allows straightforward privilege escalation
- [[tunnel]] — Network pivoting from container to host via FTP and TFTP services
- [[cron-hijack]] - Cron job hijacking via apt pre-invoke script for reverse shell

## Tools used
- [[nmap]], [[feroxbuster]], [[wfuzz]], [[davtest]], [[curl]], [[proxychains]], [[sshpass]], [[netcat]], [[nc]]
- proxychains3, tftp, ftp, hydra, ffuf, feroxbuster

## Services / ports
- [[ssh]] (22 localhost), [[http]] (80), [[squid]] (3128)
- Apache 2.4.18, dompdf 0.6.0, vsftpd 3.0.3, tftpd-hpa

## Lessons / notes
- LFI vulnerabilities can be exploited even when direct file access fails
- WebDAV can be an effective vector for webshell uploads when properly authenticated
- Forward shells are essential when outbound traffic is restricted
- Container environments often have sudo access for easy privilege escalation
- Network pivoting from containers can reveal additional attack surfaces on hosts
- Cron jobs can be hijacked by writing pre/post invoke scripts
- The box demonstrates early container-based hacking concepts
- FTP and TFTP services can be abused for file transfer and script execution
