---
type: machine
title: Certified
platform: htb
os: windows
difficulty: medium
tags: [ad, windows, privesc, adcs, acl]
solved: 2026-07-09
sources: [[htb-certified]]
related: []
---
# Certified

> Medium Windows "assume-breach" Active Directory box where starting credentials lead to ACL abuse, shadow credentials, and ESC9 ADCS exploitation for privilege escalation.

## Attack path
1. Initial credentials judith.mader → [[acl-abuse]] (WriteOwner on Management group) → add to group
2. [[shadow-credentials]] abuse → management_svc NTLM hash → [[winrm]] shell
3. GenericAll abuse → [[shadow-credentials]] again → ca_operator NTLM hash
4. [[adcs-esc9]] exploitation via CertifiedAuthentication template → administrator

## Techniques used
- [[acl-abuse]] — WriteOwner abuse on Management group to grant membership via DACL modification
- [[shadow-credentials]] — Added msDS-KeyCredentialLink to management_svc and ca_operator for authentication
- [[adcs-esc9]] — ESC9 exploitation by modifying ca_operator UPN to "Administrator" without SID
- [[genericall]] — management_svc has GenericAll over ca_operator, enabling shadow credential attack

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[netexec]] — SMB/WinRM authentication and BloodHound data collection
- [[bloodhound]] — AD privilege escalation path analysis showing WriteOwner and GenericAll rights
- [[impacket]] — owneredit.py and dacledit.py for ACL modification
- [[certipy]] — Shadow credential attacks and ESC9 exploitation
- [[evil-winrm]] — Windows remote shell access with NTLM hashes

## Services / ports
- [[smb]] (445) — Domain controller file sharing and authentication
- [[ldap]] (389/636/3268/3269) — Active Directory services
- [[kerberos]] (88) — Domain authentication services
- [[winrm]] (5985) — Windows Remote Management for shell access

## Lessons / notes
- Assume-breach scenarios start with low-privileged user credentials
- WriteOwner on groups allows taking ownership and granting membership permissions
- Shadow credentials (msDS-KeyCredentialLink) provide certificate-based authentication without password knowledge
- ESC9 requires: StrongCertificateBindingEnforcement != 2, CT_FLAG_NO_SECURITY_EXTENSION, client auth EKU, and GenericWrite over target
- ESC9 attacks modify target UPN to impersonate privileged users without valid SID mapping
- BloodHound Community Edition requires different collectors (bloodhound-python) than Classic
