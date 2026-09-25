---
type: machine
title: VulnCicada
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, kerberos, adcs, nfs, coercion, relay]
solved: 2026-07-09
sources: [[htb-vulncicada]]
related: []
---
# VulnCicada
> VulnCicada is an Active Directory box that starts with an exposed NFS share containing user profile directories. I'll find a password written on a sticky note in an image file, use it to authenticate to the domain, then exploit ADCS ESC8 by coercing the DC to authenticate via Kerberos relay to obtain a machine account certificate, and finally dump the NTDS.dit file to get the Administrator hash.

## Attack path
1. Mount exposed [[nfs]] share and exfiltrate user profile images
2. Find password in image (Cicada123) and authenticate as Rosie.Powell
3. Enumerate [[adcs]] and identify ESC8 vulnerability on web enrollment endpoint
4. Create malicious DNS record with serialized SPN pointing to attacker
5. Use [[petitpotam]] to coerce DC authentication to malicious DNS record
6. Relay Kerberos authentication to ADCS web endpoint using [[certipy]]
7. Obtain certificate as DC machine account and extract TGT plus NT hash
8. Use machine account TGT to perform [[dcsync]] and recover Administrator hash

## Techniques used
- [[nfs-enumeration]] — Mounting and enumerating exposed NFS share containing user profiles
- [[credential-from-image]] — Extracting password from sticky note in marketing.png image
- [[adcs-esc8]] — Relaying authentication to ADCS HTTP web enrollment endpoint
- [[kerberos-relay]] — Creating malicious DNS record with serialized SPN to trick DC into Kerberos authentication
- [[petitpotam]] — Coercing DC authentication via MS-EFSRPC for relay exploitation
- [[dcsync]] — Dumping NTDS.dit with machine account privileges to get Administrator hash

## Tools used
- [[nmap]] — Port scanning and service enumeration
- showmount — NFS share enumeration
- [[netexec]] — SMB/LDAP authentication and enumeration
- certipy — ADCS vulnerability scanning, Kerberos relay, and certificate operations
- bloodyAD — DNS record creation for malicious SPN
- smbserver.py (impacket) — File transfer for BulletsPassView tool
- [[wmiexec]] — Command execution as Administrator
- [[secretsdump]] — NTDS.dit hash extraction

## Services / ports
- 53/tcp — dns
- 80/tcp — [[http]] (IIS 10.0)
- 88/tcp — [[kerberos]]
- 111/tcp — rpcbind
- 135/tcp — [[rpc]]
- 139/tcp — [[smb]] (NetBIOS Session Service)
- 389/tcp — [[ldap]]
- 445/tcp — [[smb]]
- 464/tcp — kpasswd5
- 636/tcp — ldapssl
- 2049/tcp — [[nfs]]
- 3268/tcp — globalcatLDAP
- 3269/tcp — globalcatLDAPssl
- 3389/tcp — [[rdp]]
- 5985/tcp — [[winrm]] (HTTP)
- 9389/tcp — ADWS

## Lessons / notes
- NFS shares may expose user profile directories containing sensitive information
- Passwords in images: OCR or manual transcription can reveal credentials written on sticky notes
- ADCS ESC8: HTTP web enrollment endpoints are vulnerable to NTLM relay attacks
- Kerberos relay trick: Malicious DNS records with serialized SPN can trigger Kerberos authentication instead of NTLM
- PetitPotam: MS-EFSRPC authentication coercion works against Domain Controllers
- Machine account certificates: Can be used to request TGTs and perform DCSync attacks
- ESC8 from Linux: Requires malicious DNS record + coercion tool instead of Windows-only approaches
