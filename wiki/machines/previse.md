---
type: machine
title: Previse
platform: htb
os: linux
difficulty: easy
tags: [web, php, sqli, command-injection, sudo, path-hijack]
solved: 2026-07-09
sources: [[htb-previse]]
related: []
---
# Previse
> PHP file management site with execution after redirect (EAR) vulnerability to create admin account, command injection in logs processing, password cracking from database, and sudo path hijacking for root.

## Attack path
1. Bypass authentication via [[execution-after-redirect]] vulnerability
2. Create admin account and login legitimately
3. Download site backup source code
4. Identify [[command-injection]] in logs.php delimiter parameter
5. Get shell as www-data via reverse shell
6. Crack MySQL hash from database for user password
7. SSH as m4lwhere with cracked credentials
8. Abuse [[path-hijack]] in sudo script for root

## Techniques used
- [[execution-after-redirect]] — PHP redirect without exit allows accessing protected pages
- [[command-injection]] — Unsanitized delimiter parameter in exec() call
- [[hash-cracking]] — MD5crypt hash from database cracked with rockyou.txt
- [[password-reuse]] — Database password worked for SSH user
- [[path-hijack]] — Created malicious gzip script in /dev/shm, prepended to PATH
- [[sudo-misconfiguration]] — Missing secure_path in sudoers allowed PATH abuse

## Tools used
- [[nmap]]
- [[feroxbuster]]
- Burp Suite
- [[hashcat]]
- [[netexec]]
- [[netcat]]

## Services / ports
- [[ssh]] (22) — OpenSSH 7.6p1
- [[http]] (80) — Apache httpd 2.4.29

## Lessons / notes
- Execution after redirect (EAR) vulnerabilities occur when redirects don't exit
- Command injection often occurs in parameters that seem harmless (delimiter choice)
- MD5crypt hashes with emoji salts are still crackable with hashcat
- Sudo secure_path is important for preventing PATH hijacking
- MySQL credentials are often reused for user accounts
- Python scripts called from PHP may use shell commands with user input
- Setting up Burp match/replace rules automates header modification
