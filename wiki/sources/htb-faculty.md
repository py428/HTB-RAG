---
type: source
title: "HTB Faculty writeup"
raw: raw/htb-faculty.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[faculty]]
---
# Source: HTB Faculty writeup
> PHP school management system with SQL injection, mPDF file read, meta-git command injection, and gdb ptrace exploitation.

## Key facts extracted
- Both login forms vulnerable to SQL injection bypass
- mPDF 6.0 allows arbitrary file read via <annotation file="/etc/passwd">
- Database credentials: Co.met06aci.dly53ro.per
- meta-git clone vulnerable to command injection with || separators
- gdb has cap_sys_ptrace capability for arbitrary process attachment

## Filed into
[[faculty]], [[sqli]], [[mpdf-file-read]], [[command-injection]], [[ptrace-shellcode-injection]]