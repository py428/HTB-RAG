---
type: machine
title: Ypuffy
platform: htb
os: linux
difficulty: medium
tags: [linux, ad, privesc]
solved: 2026-07-09
sources: [[htb-ypuffy]]
related: []
---
# Ypuffy
> OpenBSD machine with LDAP, SMB, and SSH services. Initial access through anonymous LDAP enumeration to get NT hash, pass-the-hash to SMB for SSH key, then privilege escalation via SSH certificate signing abuse and doas permissions.
## Attack path
1. Extract NT hash from anonymous [[ldap]] enumeration for alice1978 user
2. Use pass-the-hash to access SMB share and download SSH private key
3. Convert PuTTY PPK key to OpenSSH format and SSH as alice1978
4. Abuse [[ssh-certificate-signing]] via doas permissions to sign key for root access
5. Alternative privesc via CVE-2018-14665 Xorg privilege escalation
## Techniques used
- [[ldap-enumeration]] — Anonymous LDAP bind to extract user NT hash
- [[pass-the-hash]] — SMB authentication using NTLM hash
- [[ppk-conversion]] — PuTTY PPK to OpenSSH key format conversion
- [[ssh-certificate-signing]] — CA key signing for principal authentication
- [[doas-abuse]] — SSH keygen execution as userca for certificate signing
## Tools used
- [[nmap]], [[smbclient]], puttygen, [[ssh]], [[ssh-keygen]]
## Services / ports
- [[ssh]] (22), [[http]] (80), [[smb]] (139/445), [[ldap]] (389)
## Lessons / notes
- Anonymous LDAP can reveal user NT hashes for pass-the-hash attacks
- OpenBSD uses doas instead of sudo for privilege escalation
- SSH certificate authorities allow scalable key management
- SSH principal enumeration via curl to web service
- Xorg setuid vulnerability allows arbitrary file write as root
## Alternative paths
- CVE-2018-14665: Xorg privilege escalation via font path file overwrite
