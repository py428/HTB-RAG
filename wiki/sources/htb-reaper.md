---
type: source
title: "HTB Reaper writeup"
raw: raw/htb-reaper.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[reaper]]
---
# Source: HTB Reaper writeup
> Windows pwn chain starting with format string leak and buffer overflow to shell, then kernel driver exploitation for SYSTEM via token manipulation.

## Key facts extracted
- Binary dev_keysvc.exe on FTP with buffer overflow (88-byte offset) and format string vulnerability
- Format string in log_key function allows memory leak via %p to bypass ASLR
- ROP chain uses VirtualAlloc to make stack executable then jumps to msfvenom shellcode
- reaper.sys kernel driver provides arbitrary read/write via IOCTL 0x8000200b
- Token theft copies SYSTEM process token to current process for privilege escalation

## Filed into
[[reaper]], [[format-string]], [[buffer-overflow]], [[rop]], [[kernel-token-theft]], [[arbitrary-read]], [[arbitrary-write]]