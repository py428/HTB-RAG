---
type: machine
title: Bolt
platform: htb
os: linux
difficulty: medium
tags: [docker, web, ssti, ad, passbolt, linux, privesc]
solved: 2026-07-09
sources: [[htb-bolt]]
related: []
---
# Bolt
> Multi-stage web exploitation box featuring Docker image analysis, server-side template injection (SSTI) in Flask/Jinja2, Active Directory password reuse, and abuse of a Passbolt password manager to obtain root credentials.

## Attack path
1. Download and analyze Docker image from website to extract SQLite database and source code
2. Crack admin hash from database to access demo site (invite code: XNSS-HSJW-3NGU-8XTJ)
3. Exploit [[ssti]] in profile name field via email confirmation to get shell as www-data
4. Reuse database password to SSH as user eddie
5. Extract Passbolt private key from Chrome extension data, crack it with john
6. Use database access to generate account recovery link, access Passbolt to get root password

## Techniques used
- [[docker-image-analysis]] — Extract secrets and source code from Docker image layers using dive
- [[ssti]] — Jinja2 template injection in Flask email confirmation via profile name field
- [[password-reuse]] — Database credentials reused for SSH access
- [[passbolt-abuse]] — Extract and crack PGP key from Chrome extension to access password manager

## Tools used
- [[nmap]], [[dive]], [[hashcat]], [[feroxbuster]], [[ffuf]], [[gobuster]], [[john]], [[netcat]]

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 80/tcp — [[http]] — nginx (bolt.htb, demo.bolt.htb, mail.bolt.htb)
- 443/tcp — [[https]] — Passbolt (passbolt.bolt.htb)

## Lessons / notes
- Docker images can contain sensitive data in previous layers even after "deletion"
- SSTI payloads in Jinja2 can use {{ namespace.__init__.__globals__.os.popen('cmd').read() }} for execution
- Passbolt stores private keys in Chrome extension local storage at Local Extension Settings/<id>
- Database access allows generating password recovery tokens by extracting from authentication_tokens table
