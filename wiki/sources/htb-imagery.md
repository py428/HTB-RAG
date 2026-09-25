---
type: source
title: "HTB Imagery writeup"
raw: raw/htb-imagery.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[imagery]]
---
# Source: HTB Imagery writeup
> Detailed writeup for HTB Imagery machine covering XSS exploitation, directory traversal, command injection, database credential extraction, encrypted backup forensics, and sudo abuse for root access.

## Key facts extracted
- Target: Imagery image gallery Flask application
- Primary attack vector: XSS → Directory traversal → Command injection → Backup forensics → Sudo abuse
- Initial foothold: Stored XSS in bug report feature for admin cookie theft
- Privilege escalation: Custom charcol backup utility with sudo permissions
- Database access: SQLite database with MD5 password hashes
- Root access: Encrypted backup recovery and custom backup utility exploitation
- The box demonstrates multiple realistic web application vulnerabilities

## Filed into
[[imagery]], [[xss]], [[directory-traversal]], [[command-injection]], [[password-cracking]], [[backup-forensics]], [[sudo]], [[adcs-template-abuse]]
