---
type: machine
title: Sea
platform: htb
os: linux
difficulty: easy
tags: [web, privesc, linux, wondercms, ssh]
solved: 2026-07-09
sources: [[htb-sea]]
related: []
---
# Sea
> Sea is an easy Linux box running WonderCMS with a vulnerable contact form that allows XSS exploitation. The attack path involves exploiting stored XSS to upload a malicious theme as an admin user, cracking the WonderCMS admin password from the database, and finding an internal monitoring panel with command injection vulnerability. Alternative paths include brute-forcing the admin password and exploiting the same internal panel for root access.

## Attack path
1. [[nmap]] enumeration reveals SSH and HTTP services
2. [[feroxbuster]] identifies WonderCMS installation and login page at `/loginURL`
3. Discover contact form vulnerable to [[stored-xss]] - admin visits URLs submitted in form
4. Exploit [[cve-2023-41425]] - use XSS to upload malicious theme with webshell
5. Access WonderCMS database file and extract bcrypt hash for admin password
6. Crack password with [[hashcat]] to obtain credentials for user amay
7. SSH into box as amay and discover internal monitoring service on localhost:8080
8. Exploit [[command-injection]] in log analysis functionality - inject commands via file parameter
9. Use command injection to add SSH key to `/root/.ssh/authorized_keys` for root access

## Techniques used
- [[stored-xss]] — Contact form allows JavaScript injection that executes when admin visits submitted URLs
- [[theme-upload-exploit]] — Use XSS to trigger installation of malicious theme containing PHP webshell
- [[bcrypt-cracking]] — Extract and crack bcrypt hash from WonderCMS database.js file
- [[command-injection]] — Internal monitoring panel vulnerable to command injection via log file parameter

## Tools used
[[nmap]], [[feroxbuster]], [[ffuf]], [[hashcat]], [[netexec]], [[hydra]], [[nc]], [[curl]]

## Services / ports
22/tcp — [[ssh]], 80/tcp — [[http]] (Apache/WonderCMS)

## Lessons / notes
- WonderCMS stores configuration in database.js file including bcrypt-hashed passwords
- Internal services on localhost may have different authentication requirements than external ones
- Command injection in log file analysis can be exploited using comment characters to bypass remaining filters
- XSS exploitation requires finding a trigger mechanism - in this case, a headless browser visiting contact form URLs
