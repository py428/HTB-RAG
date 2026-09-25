---
type: source
title: "HTB Aragog writeup"
raw: raw/htb-aragog.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[aragog]]
---
# Source: HTB Aragog writeup
> Complete walkthrough of a medium Linux box demonstrating XXE exploitation and WordPress credential capture techniques.

## Key facts extracted
- Aragog runs Ubuntu 16.04 with FTP, SSH, and Apache web services
- Anonymous FTP access provides XML file showing expected input structure
- hosts.php endpoint processes XML input and returns subnet calculations
- XXE injection allows reading arbitrary files from filesystem
- Florian user's SSH private key accessible via XXE at /home/florian/.ssh/id_rsa
- WordPress dev_wiki directory with backup process running every 5 minutes
- wp-login.py script runs as cliff user, authenticating to WordPress every minute
- Modifying wp-login.php allows credential capture when script runs
- Root credentials: Administrator / !KRgYs(JFO!&MTr)lf

## Filed into
[[aragog]], [[xxe]], [[ssh-key-reuse]], [[web-shell-upload]]
