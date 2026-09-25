---
type: source
title: "HTB Zipping writeup"
raw: raw/htb-zipping.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[zipping]]
---
# Source: HTB Zipping writeup
> Detailed writeup covering Zipping watch store exploitation including zip symlink file reads, PHP filter bypass for SQL injection, MySQL FILE privilege abuse for webshells, and privilege escalation via shared library hijacking.

## Key facts extracted
- File upload accepts zip archives containing symlinks for arbitrary file reads
- PHP preg_match filtering bypassable with newline characters
- MySQL database running as root with FILE privilege enabled
- PHP LFI with file_exists check bypassable via phar:// wrapper
- SUID stock binary loads libcounter.so from user-writable .config directory

## Filed into
[[zipping]], [[zip-symlink-file-read]], [[php-filter-bypass]], [[mysql-file-write]], [[lfi-exploitation]], [[shared-library-hijacking]]