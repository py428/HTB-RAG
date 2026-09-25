---
type: source
title: "HTB Browsed writeup"
raw: raw/htb-browsed.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[browsed]]
---
# Source: HTB Browsed writeup
> Detailed analysis of a Linux browser extension testing platform. The writeup covers discovering internal services through Chrome debug logs, exploiting a Flask application via SSRF using malicious Chrome extensions, achieving RCE through Bash arithmetic evaluation injection, and elevating to root via Python bytecode cache poisoning in a world-writable __pycache__ directory.

## Key facts extracted
- Chrome extensions tested in headless Chrome with debug logs leaked to user
- Internal Gitea instance at browsedinternals.htb contained MarkdownPreview Flask app source
- Flask app on localhost:5000 had Bash arithmetic evaluation vulnerability in routines.sh
- World-writable __pycache__ directory allowed poisoning .pyc files executed by sudo
- Python bytecode cache format includes 16-byte header followed by marshaled code object

## Filed into
[[browsed]], [[ssrf]], [[command-injection]], [[python-cache-poisoning]]
