---
type: machine
title: Fortune
platform: htb
os: linux
difficulty: insane
tags: [openbsd, web, privesc, nfs, authpf]
solved: 2026-07-09
sources: [[htb-fortune]]
related: []
---
# Fortune
> Fortune is an insane difficulty OpenBSD box focused on exploiting authpf, NFS, and command injection to gain initial access, then leveraging pgadmin database credentials for privilege escalation.

## Attack path
1. [[command-injection]] in fortune web application to get RCE as www-data
2. Find CA certificate and key to generate client certificate for HTTPS access
3. Access authpf with SSH key to open firewall ports
4. [[nfs]] access with [[uid-spoofing]] to access user home directories
5. Extract credentials from pgadmin database for root access

## Techniques used
- [[command-injection]] — Exploiting fortune command injection in OpenBSD httpd
- [[certificate-abuse]] — Using found CA cert/key to create client certificates
- [[authpf-bypass]] — Using authpf to dynamically open firewall ports
- [[nfs]] — Exploiting NFS with uid spoofing to access user files
- [[database-credential-extraction]] — Extracting PostgreSQL dba credentials from pgadmin

## Tools used
[[nmap]], openssl, curl, smbclient, showmount, nc, python

## Services / ports
- 22/tcp — [[ssh]]
- 80/tcp — [[http]] (OpenBSD httpd)
- 443/tcp — [[https]] (requires client certificate)
- 111/tcp — rpcbind
- 613/tcp — mountd
- 2049/tcp — [[nfs]]
- 8081/tcp — [[http]] (pgadmin4)

## Lessons / notes
- OpenBSD uses pf (packet filter) instead of iptables
- authpf allows users to dynamically modify firewall rules via SSH
- NFS with root_squash can be bypassed using uid spoofing
- pgadmin stores encrypted passwords that can be decrypted with user password hashes
- The box demonstrates a complex multi-stage attack involving certificate-based authentication
