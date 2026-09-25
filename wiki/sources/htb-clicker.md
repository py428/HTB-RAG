---
type: source
title: "HTB Clicker writeup"
raw: raw/htb-clicker.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[clicker]]
---
# Source: HTB Clicker writeup
> PHP mass assignment exploitation with multiple bypass methods, webshell creation via unchecked file extensions, setuid binary abuse for SSH key exfiltration, and three different privilege escalation paths via sudo script environment variables.

## Key facts extracted
- NFS /mnt/backups share contains clicker.htb_backup.zip source code
- save_game.php mass assignment blocked on 'role' but bypassable with newline or SQLi
- export.php allows arbitrary file extensions for webshell creation
- execute_query setuid binary reads files via directory traversal in SQL filename
- monitor.sh sudo script preserves environment variables (SETENV flag)
- Three privesc paths: PERL5OPT debug, http_proxy XXE, LD_PRELOAD library

## Filed into
[[clicker]], [[mass-assignment]], [[newline-injection]], [[file-upload]], [[setuid]], [[perl-debug]], [[xxe]], [[ld-preload]]
