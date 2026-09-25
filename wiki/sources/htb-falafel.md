---
type: source
title: "HTB Falafel writeup"
raw: raw/htb-falafel.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[falafel]]
---
# Source: HTB Falafel writeup
> Comprehensive 0xdf writeup covering the complete attack chain from SQL injection and type juggling to framebuffer screenshot extraction and disk group privsec. Shows both manual exploitation and tool-assisted approaches.
## Key facts extracted
- PHP application with login form vulnerable to blind SQL injection (different response for existing vs non-existing users)
- Magic hash "240610708" bypasses authentication due to PHP type juggling with MD5 hashes starting with "0e"
- File upload truncates long filenames, allowing .php.png to be shortened to .php
- Video group membership enables /dev/fb0 framebuffer reading to capture user's screen
- Disk group provides raw disk access for root flag extraction
## Filed into
[[falafel]], [[sqli]], [[type-juggling]], [[file-upload-truncation]], [[framebuffer]], [[disk-group]]
