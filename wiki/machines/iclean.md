---
type: machine
title: IClean
platform: htb
os: linux
difficulty: medium
tags: [linux, web, flask, xss, ssti, rce, password-cracking, sudo, privesc, file-read]
solved: 2026-07-09
sources: [[htb-iclean]]
related: []
---
# IClean
> IClean is a Flask-based cleaning company website vulnerable to XSS and server-side template injection. The attack path involves stealing admin cookies via XSS, exploiting SSTI for RCE, cracking database hashes for horizontal movement, and abusing sudo permissions on a PDF tool to read arbitrary files including SSH keys for root access.

## Attack path
1. [[xss]] — Stored XSS in quote form to steal admin session cookie
2. [[ssti]] — Server-SI Template Injection in QR code generation for RCE
3. [[password-cracking]] — Crack SHA256 hashes from database using CrackStation
4. [[sudo]] — Exploit sudo access to qpdf tool for arbitrary file read
5. [[file-read]] — Read SSH keys and root flag via PDF attachment exploitation

## Techniques used
- [[xss]] — Stored XSS in contact form to steal admin Flask session cookie
- [[ssti]] — Server-Side Template Injection in QR code generation using Jinja2
- [[rce]] — Remote code execution via SSTI payload with base64-encoded reverse shell
- [[password-cracking]] — Crack SHA256 database password hashes using CrackStation
- [[sudo]] — Abuse sudo permissions on qpdf PDF tool for file read
- [[file-read]] — Arbitrary file read via PDF attachment creation

## Tools used
- [[nmap]], [[feroxbuster]], [[curl]], [[flask-unsign]], [[hashcat]], [[evil-winrm]]
- crackstation.net, CyberChef, qpdf, 7z2john.pl, john, sqlite3

## Services / ports
- [[ssh]] (22), [[http]] (80), [[winrm]] (5985)
- Apache 2.4.52, Werkzeug/2.3.7 Python/3.10.12, Flask application

## Lessons / notes
- XSS exploitation requires identifying non-HttpOnly session cookies
- SSTI payloads need to bypass common filters - using hex encoding and attr chaining
- Flask applications often store database credentials in application source code
- PDF tools can be abused for file reads even with limited permissions
- Hash cracking can be done with online tools like CrackStation for common hashes
- The box demonstrates realistic web application vulnerabilities in a business context
