---
type: machine
title: Investigation
platform: htb
os: linux
difficulty: medium
tags: [web, linux, forensics, privesc]
solved: 2026-07-09
sources: [[htb-investigation]]
related: []
---
# Investigation is a medium Linux box themed around digital forensics, featuring an image upload service that processes files with Exiftool. The exploitation leverages a command injection vulnerability in Exiftool, followed by Windows event log analysis to extract credentials, and abuse of a custom binary that downloads and executes scripts for root access.

## Attack path
1. [[exiftool-cve-2022-23935]] via filename pipe character for RCE
2. [[evtx-analysis]] to extract password from Windows security event logs
3. [[binary-abuse]] via custom /usr/bin/binary that downloads and executes scripts

## Techniques used
- [[exiftool-cve-2022-23935]] — Command injection via filename ending with pipe character
- [[evtx-analysis]] — Converting and analyzing Windows event logs for credentials
- [[base64-encoding]] — Bypassing command character restrictions
- [[binary-abuse]] — Abusing curl-based binary that executes downloaded scripts
- [[race-condition]] — Exploiting timing between file download and execution

## Tools used
- [[nmap]] — Port scanning and service version detection
- [[feroxbuster]] — Directory enumeration with file extension fuzzing
- Python webserver — Hosting exploit scripts and payloads
- [[netcat]] — Shell handling and file transfer
- msgconvert — Converting Outlook .msg files to mbox format
- mutt — Reading email messages and attachments
- evtx_dump — Converting Windows event logs to JSON format
- [[jq]] — Parsing and filtering JSON event log data
- openssl — Password hash generation for testing

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 80/tcp — [[http]] — Apache 2.4.41 with Exiftool processing
- 3306/tcp — MySQL (localhost only)
- 54321/tcp — Python Flask notification server (localhost only)

## Lessons / notes
- Exiftool before 12.38 vulnerable to command injection via filenames ending with |
- Windows event logs can contain sensitive data like typed passwords
- Event ID 4625 (failed login) may contain passwords typed in username field
- Converting .evtx to JSON enables easier log analysis with jq
- Custom binaries that download and execute scripts are ripe for abuse
- Race conditions possible between file write and execution in automated systems
- Perl's open() command treats filenames ending with | as commands to execute