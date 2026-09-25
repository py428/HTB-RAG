---
type: machine
title: Bookworm
platform: htb
os: linux
difficulty: insane
tags: [web, xss, idor, file-upload, symlink, sqli, postscript, linux, privesc]
solved: 2026-07-09
sources: [[htb-bookworm]]
related: []
---
# Bookworm
> Complex multi-stage exploitation chain combining XSS, IDOR, insecure file upload, directory traversal, symlink abuse, SQL injection, and PostScript injection for complete system compromise.

## Attack path
1. Register account, upload JavaScript as avatar with image/png MIME type
2. Use [[idor]] in basket edit to inject XSS payload into other users' baskets
3. Enumerate profile and order pages via XSS, identify /download endpoint
4. Exploit [[directory-traversal]] in multi-file download to read arbitrary files via ZIP
5. Extract database credentials from source code leak, SSH as frank
6. Use [[symlink-abuse]] in ebook converter to write SSH key to neil's authorized_keys
7. Exploit [[sqli]] in sudo genlabel script for [[postscript-injection]] file write
8. Write SSH key to /root/.ssh/authorized_keys or read root's private key

## Techniques used
- [[xss-csp-bypass]] — Upload malicious JS as avatar, bypass script-src 'self' CSP
- [[idor]] — Access/edit other users' baskets by enumerating IDs from /shop comments
- [[directory-traversal]] — Traverse via bookIds parameter in multi-file ZIP download
- [[symlink-abuse]] — Create symlink from non-protected directory to bypass protected_symlinks
- [[postscript-injection]] — Inject PostScript via SQLi for file read/write with -dNOSAFER

## Tools used
- [[nmap]], [[feroxbuster]], [[ffuf]], [[netexec]], [[ssh]], [[ps2pdf]]

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 80/tcp — [[http]] — nginx (Express.js bookstore)
- 3001/tcp — [[http]] — Express.js ebook converter (localhost only)

## Lessons / notes
- Express handles ?id=1&id=2 as array, ?id=1 as string
- protected_symlinks=1 prevents following symlinks in world-writable directories with different UIDs
- ebook-convert creates directories for output without extension
- PostScript -dNOSAFER allows file I/O operations
- SQLite development version, MariaDB in production
