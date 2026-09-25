---
type: machine
title: Reaper
platform: htb
os: windows
difficulty: insane
tags: [windows, buffer-overflow, format-string, kernel, rop, ad]
solved: 2026-07-09
sources: [[htb-reaper]]
related: []
---
# Reaper
> Windows pwn challenge with format string vulnerability and buffer overflow leading to shell, then kernel driver exploitation for arbitrary read/write and token theft to SYSTEM.

## Attack path
1. Exploit [[format-string]] vulnerability to leak memory address and bypass ASLR
2. Chain [[buffer-overflow]] with [[rop]] using VirtualAlloc to get shellcode execution as keysvc
3. Analyze and exploit kernel driver reaper.sys for [[arbitrary-read]] and [[arbitrary-write]]
4. Perform [[kernel-token-theft]] by copying SYSTEM token to current process

## Techniques used
- [[format-string]] — Leaked memory address via %p in key validation to bypass ASLR
- [[buffer-overflow]] — 88-byte offset in key activation to control RIP
- [[rop]] — VirtualAlloc chain to make stack executable and return to shellcode
- [[kernel-token-theft]] — Used driver IOCTLs to copy SYSTEM process token to current process

## Tools used
[[nmap]], [[ftp]], [[ropper]], [[gdb]], [[pwntools]], [[msfvenom]], x64dbg

## Services / ports
[[ftp]] (21), [[http]] (80), [[rdp]] (3389), custom-key-service (4141)

## Lessons / notes
- NX/DEP enabled on binary requiring ROP with VirtualAlloc to make stack executable
- Format string vulnerability in snprintf allowed memory leak for ASLR bypass
- Kernel driver provided arbitrary read/write primitives via IOCTL 0x8000200b
- Token theft required finding EPROCESS structure offsets for Windows 10 via kernel debugging