---
type: source
title: "HTB Rainbow writeup"
raw: raw/htb-rainbow.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[rainbow]]
---
# Source: HTB Rainbow writeup
> Detailed exploit development guide for Windows custom webserver buffer overflow with x32dbg crash analysis, bad character filtering, and weaponization, followed by fodhelper UAC bypass technique to achieve elevated privileges.

## Key facts extracted
- Custom Rainbow webserver on TCP 8080 vulnerable to buffer overflow in HTTP request handling
- Anonymous FTP provides rainbow.exe binary and development documentation
- x32dbg used for crash analysis, breakpoint setting, and exploit development
- Bad character filtering requires removing null bytes, newlines, and other problematic characters
- fodhelper UAC bypass leverages Windows Registry manipulation to execute commands with high integrity
- User in Administrators group but UAC blocks access to sensitive files like root.txt

## Filed into
[[rainbow]], [[buffer-overflow]], [[fodhelper]], [[uac-bypass]], [[windows-exploit-dev]], [[x32dbg]]