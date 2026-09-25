---
type: machine
title: TombWatcher
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, privesc, adcs]
solved: 2026-07-09
sources: [[htb-tombwatcher]]
related: []
---
# TombWatcher
> TombWatcher is an assume-breach Active Directory box focused on BloodHound analysis and ADCS exploitation. Starting with initial credentials, the attack path leverages targeted Kerberoasting, GMSA password recovery, shadow credentials, and ESC15 for Domain Administrator access.
## Attack path
1. Use [[targeted-kerberoast]] to compromise Alfred account from Henry's WriteSPN access
2. Exploit [[gmsa-password-recovery]] by adding Alfred to Infrastructure group
3. Use [[force-change-password]] as ANSIBLE_DEV$ to compromise Sam
4. Leverage [[shadow-credentials]] from Sam's WriteOwner over John
5. Recover deleted [[ad-recycle-bin]] cert_admin account using John's GenericAll over ADCS
6. Exploit [[ESC15]] (CVE-2024-49019) as cert_admin for Domain Administrator access
## Techniques used
- [[targeted-kerberoast]] — Adding SPN to user account for Kerberoasting with hashcat cracking
- [[gmsa-password-recovery]] — Reading GMSA passwords from group membership
- [[force-change-password]] — Resetting user passwords via LDAP write access
- [[shadow-credentials]] — Adding Key Credential Link for certificate-based authentication
- [[ad-recycle-bin]] — Recovering deleted AD objects with appropriate permissions
- [[ESC15]] — Arbitrary application policy injection in v1 certificate templates
## Tools used
[[nmap]], [[netexec]], [[bloodhound]], [[rusthound-ce]], [[hashcat]], [[certipy]], [[bloodyAD]], [[evil-winrm]]
## Services / ports
- [[ldap]] (389, 636, 3268, 3269)
- [[kerberos]] (88, 464)
- [[smb]] (445)
- [[winrm]] (5985)
- [[http]] (80) - IIS 10.0
- [[dns]] (53)
## Lessons / notes
- BloodHound analysis reveals complex AD attack paths with multiple privilege escalation techniques
- Targeted Kerberoasting is effective when WriteSPN access is available
- GMSA passwords can be recovered with appropriate group memberships
- Shadow credentials provide elegant alternative to password-based attacks
- AD Recycle Bin allows recovery of deleted accounts with proper permissions
- ESC15 vulnerability allows arbitrary EKU injection in v1 certificate templates
