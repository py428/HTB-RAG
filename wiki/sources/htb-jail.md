---
type: source
title: "HTB Jail writeup"
raw: raw/htb-jail.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[jail]]
---
# Source: HTB Jail writeup
> Insane difficulty Linux machine with multi-stage exploitation: buffer overflow with execstack, NFS abuse, rvim escape, Atbash cipher, RSA key recovery. Teaches diverse techniques from binary exploitation to cryptography.

## Key facts extracted
- Custom jail service on TCP 7411: USER/PASS auth with DEBUG mode
- DEBUG mode leaks static buffer address: 0xffffd610
- Buffer overflow at 28-byte offset, execstack enabled for shellcode execution
- NFS shares: /opt (logreader script) and /var/nfsshare (writable)
- no_all_squash allows setuid binary creation as frank (uid 1000)
- rvim (restricted vim) escape via Python execution
- RAR password: Morris1962! (Frank Morris + escape year + symbol)
- RSA public key cracked using Wiener's attack (small d vulnerability)
- SELinux contexts present but not blocking exploitation

## Filed into
[[jail]], [[buffer-overflow]], [[nfs-abuse]], [[rvim-escape]], [[rsa-key-recovery]]
