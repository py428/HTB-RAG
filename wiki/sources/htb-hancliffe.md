---
type: source
title: "HTB Hancliffe writeup"
raw: raw/htb-hancliffe.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[hancliffe]]
---
# Source: HTB Hancliffe writeup
> Complex Windows exploit chain involving URI normalization bypass for Nuxeo SSTI, Unified Remote protocol exploitation, Firefox credential extraction, and custom buffer overflow with socket reuse.

## Key facts extracted
- NGINX proxy configuration allows bypass via `/maintenance/..;/` due to different URI handling between nginx and Java
- Nuxeo 10.2 vulnerable to Java SSTI in login.jsp with template syntax execution
- Unified Remote 3.9.0.2463 listens on ports 9510/9512 with binary protocol for sending keystrokes
- Firefox profile contains saved H@$hPa$$ credentials encrypted in key4.db + logins.json
- MyFirstApp.exe has strcpy overflow in _SaveCreds function with 80-byte buffer receiving unlimited input
- Socket reuse technique retrieves socket descriptor from stack and calls recv to stage larger shellcode

## Filed into
[[hancliffe]], [[uri-normalization]], [[ssti]], [[unified-remote]], [[firefox-credentials]], [[buffer-overflow]], [[socket-reuse]]
