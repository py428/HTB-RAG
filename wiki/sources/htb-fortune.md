---
type: source
title: "HTB Fortune writeup"
raw: raw/htb-fortune.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[fortune]]
---
# Source: HTB Fortune writeup
> Complete writeup for Fortune HTB machine covering command injection, certificate-based authentication, NFS exploitation, and pgadmin credential extraction.

## Key facts extracted
- OpenBSD 6.4 system with custom fortune web application
- Command injection in fortune DB selection parameter
- CA certificate and key stored in /home/bob/ca/intermediate/
- authpf used for dynamic firewall rule modification
- NFS export of /home directory with uid spoofing possible
- pgadmin4 database containing encrypted dba credentials

## Filed into
[[fortune]], [[command-injection]], [[nfs]], [[certificate-abuse]], [[database-credential-extraction]]
