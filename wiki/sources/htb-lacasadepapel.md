---
type: source
title: "HTB LaCasaDePapel writeup"
raw: raw/htb-lacasadepapel.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[lacasadepapel]]
---
# Source: HTB LaCasaDePapel writeup
> Comprehensive walkthrough of LaCasaDePapel, an easy HTB box featuring a modified VSFTPD backdoor. The writeup covers exploiting the FTP backdoor to access Psy Shell, extracting CA keys for mutual TLS authentication, path traversal for SSH key retrieval, and supervisor configuration abuse for root access.

## Key facts extracted
- **Modified VSFTPD**: Backdoor opens Psy Shell on port 6200 and adds iptables rule for attacker IP
- **Psy Shell**: PHP debugging REPL running as root with system(), exec(), shell_exec() disabled
- **CA key location**: /home/nairobi/ca.key contains private key for signing client certificates
- **Mutual TLS**: HTTPS site requires client certificate signed by CA with CN=lacasadepapel.htb
- **Path traversal**: Private area accepts base64-encoded file paths for arbitrary file read
- **SSH key**: Berlin's SSH private key in ~/.ssh/ works for professor user
- **Supervisor**: Root-run supervisor includes /home/professor/*.ini config files

## Filed into
[[lacasadepapel]], [[vsftpd-backdoor]], [[psy-shell]], [[ca-key-theft]], [[mutual-tls-auth]], [[path-traversal]], [[supervisor-ini-replacement]]