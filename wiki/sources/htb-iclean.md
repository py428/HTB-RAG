---
type: source
title: "HTB IClean writeup"
raw: raw/htb-iclean.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[iclean]]
---
# Source: HTB IClean writeup
> Detailed writeup for HTB IClean machine covering XSS exploitation, Server-Side Template Injection, database credential extraction, and sudo abuse for PDF file reading.

## Key facts extracted
- Target: IClean cleaning company Flask application
- Primary attack vector: XSS for admin access, then SSTI for RCE
- Initial foothold: Stored XSS in contact form bypasses input sanitization
- Privilege escalation: Sudo permissions on qpdf tool for arbitrary file read
- Database access: MySQL credentials found in Flask application source code
- Root access: SSH keys extracted via PDF attachment exploitation
- The box demonstrates realistic web application vulnerabilities in a business context

## Filed into
[[iclean]], [[xss]], [[ssti]], [[rce]], [[password-cracking]], [[sudo]], [[file-read]]
