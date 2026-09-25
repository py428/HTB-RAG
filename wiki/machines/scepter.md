---
type: machine
title: Scepter
platform: htb
os: windows
difficulty: hard
tags: [ad, privesc, certificate, kerberos]
solved: 2026-07-09
sources: [[htb-scepter]]
related: []
---
# Scepter
> Scepter is a hard Active Directory box focused on certificate authentication abuse. Starting with NFS-share exposed client certificates, you'll crack PFX passwords, authenticate via PKINIT, escalate through ESC14 certificate abuses, and eventually achieve DCSync for full domain compromise.

## Attack path
1. Mount NFS share, extract certificate authentication files
2. Crack PFX and PEM passwords (all "newpassword") using john/hashcat  
3. Authenticate as d.baker via PKINIT certificate authentication
4. Use BloodHound to find ForceChangePassword privilege over a.carter
5. Change a.carter password, authenticate with new credentials
6. Abuse ESC14: Modify d.baker email to match h.brown's altSecurityIdentities
7. Request certificate as d.baker with h.brown email, auth as h.brown via PKINIT
8. Repeat ESC14 to auth as p.adams (member of Replication Operators)
9. [[dcsync]] as p.adams to dump domain hashes

## Techniques used
- [[nfs-enumeration]] — Open NFS share exposes client authentication certificates  
- [[certificate-authentication]] — PKINIT authentication with client certificates
- [[password-cracking]] — PFX and PEM password cracking with john/hashcat
- [[force-change-password]] — d.baker has ForceChangePassword over a.carter
- [[esc14]] — Certificate abuse via altSecurityIdentities mapping
- [[dcsync]] — p.adams in Replication Operators allows credential dump

## Tools used
showmount, [[openssl]], [[john]], [[hashcat]], [[certipy]], [[netexec]], [[bloodhound]], [[bloodyAD]], [[secretsdump]], [[evil-winrm]]

## Services / ports
- [[dns]] (53) — Simple DNS Plus
- [[kerberos]] (88) — Microsoft Windows Kerberos
- [[nfs]] (2049) — Open NFS share /helpdesk with certificates
- [[ldap]] (389, 636) — Microsoft Windows Active Directory LDAP
- [[smb]] (445) — Microsoft-ds
- [[winrm]] (5985, 5986) — WinRM access with Kerberos

## Lessons / notes
- Three certificates (clark.pfx, lewis.pfx, scott.pfx) have revoked accounts
- d.baker certificate (baker.crt/key) provides initial authentication
- ESC14 abuse involves setting user email to match target's altSecurityIdentities
- SubjectAltRequireEmail flag in certificate template enables ESC14
- Protected Users group prevents NTLM authentication, requires Kerberos
- CMS group has WriteProperty on altSecurityIdentities for escalation
- Certificate auth bypasses account disabled/password expired restrictions
