---
type: machine
title: Browsed
platform: htb
os: linux
difficulty: medium
tags: [linux, web, ssrf, chrome-extension, python, privesc, sudo]
solved: 2026-07-09
sources: [[htb-browsed]]
related: []
---
# Browsed
> Linux box hosting a browser extension repository where uploaded extensions are tested in a headless Chrome instance. Internal services discovered through Chrome debug logs lead to SSRF against a Flask application with Bash arithmetic evaluation injection, followed by Python bytecode cache poisoning for privilege escalation.

## Attack path
1. [[ssrf]] — Chrome extension background worker to reach internal Flask app on localhost:5000
2. [[command-injection]] — Bash arithmetic evaluation via `-eq` comparison in routines.sh
3. [[python-cache-poisoning]] — Poison world-writable __pycache__ to get code execution as root via sudo

## Techniques used
- [[ssrf]] — Chrome extension background service worker bypasses CORS to reach internal Flask app
- [[command-injection]] — Bash arithmetic evaluation injection using `a[$(command)]` syntax in -eq comparisons
- [[python-cache-poisoning]] — Overwrite .pyc files in world-writable __pycache__ directory to execute code as root

## Tools used
[[nmap]], [[feroxbuster]], chrome browser, zip, [[python3.12]], [[netcat]], base64, xxd

## Services / ports
[[ssh]] (22), [[http]] (80 - nginx)

## Lessons / notes
- Chrome debug logs reveal internal services like browsedinternals.htb (Gitea) and localhost:5000 (Flask)
- Chrome extensions with background service workers can make requests to any URL without CORS restrictions
- Bash arithmetic evaluation with -eq can be abused for command injection using array subscript syntax
- Python's __pycache__ bytecode caching can be poisoned when the directory is world-writable
- .pyc files have a 16-byte header followed by marshaled code object
- Sudo allowed a Python script that imported from a world-writable __pycache__ directory
