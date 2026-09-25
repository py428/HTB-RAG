---
type: machine
title: Infiltrator
platform: htb
os: windows
difficulty: insane
tags: [windows, ad, kerberos, as-rep-roasting, bloodhound, acl-genericall, acl-forcechangepassword, gmsa, adcs-template-abuse, rdp, ssh, calendar-execution, pcaps, bitlocker, dcsync, ntds, tunneling]
solved: 2026-07-09
sources: [[htb-infiltrator]]
related: []
---
# Infiltrator
> Infiltrator is an insane-difficulty Windows Active Directory domain environment with a complex attack chain. The path involves AS-REP roasting for initial credentials, BloodHound-guided ACL abuse for lateral movement, Output Messenger exploitation, calendar-based code execution, PCAP analysis for credential extraction, BitLocker recovery, NTDS dumping, and ADCS ESC4 exploitation for domain administrator access.

## Attack path
1. [[kerberos-username-enumeration]] — Username enumeration using website names and kerbrute
2. [[as-rep-roasting]] — AS-REP roasting L.clark account for initial credentials
3. [[password-reuse]] — Password reuse to access D.Anderson with Kerberos authentication
4. [[acl-genericall]] — GenericAll on Marketing Digital OU via dacledit.py modification
5. [[shadow-credentials]] — Shadow credentials abuse using certipy for E.Rodriguez access
6. [[acl-forcechangepassword]] — Force change password on M.Harris via group membership
7. [[rdp-initial-access]] — RDP access via M.Harris credentials
8. [[calendar-execution]] — Code execution via Output Messenger calendar automation
9. [[tunnel]] — Network tunneling via Chisel to access internal services
10. [[api-abuse]] — Output Messenger API exploitation for credential extraction
11. [[bitlocker]] — BitLocker recovery key extraction from encrypted backup archive
12. [[dcsync]] — NTDS hash extraction from backed up registry hive using secretsdump
13. [[gmsa]] — ReadGMSAPassword abuse to dump infiltrator_svc$ gMSA hash
14. [[adcs-template-abuse]] — ADCS ESC4 template abuse via certipy for administrator access

## Techniques used
- [[kerberos-username-enumeration]] — Username format enumeration from website names using kerbrute
- [[as-rep-roasting]] — AS-REP roasting for initial credential acquisition
- [[password-reuse]] — Password reuse across multiple domain accounts
- [[acl-genericall]] — ACL abuse via GenericAll on Organizational Unit for user compromise
- [[shadow-credentials]] — Shadow credentials using Key Credential Link injection via certipy
- [[acl-forcechangepassword]] — Force change password via group membership and ACL abuse
- [[rdp-initial-access]] — Initial RDP access and credential theft
- [[calendar-execution]] — Scheduled task execution via Output Messenger calendar automation
- [[tunnel]] — Network tunneling with Chisel to access internal services
- [[api-abuse]] — API key abuse for Output Messenger data extraction
- [[bitlocker]] — BitLocker recovery key usage for encrypted drive access
- [[dcsync]] — Domain Controller Sync using secretsdump on NTDS.dit backup
- [[gmsa]] — Group Managed Service Account password extraction using netexec
- [[adcs-template-abuse]] — ADCS ESC4 template abuse for certificate enrollment

## Tools used
- [[nmap]], [[kerbrute]], [[netexec]], [[impacket]], [[bloodhound-python]], [[dacledit.py]], [[certipy]], [[bloodyAD]], [[chisel]], [[msfvenom]], [[evil-winrm]], [[rdesktop]]
- username-anarchy, GetNPUsers.py, getTGT.py, changepasswd.py, secretsdump.py, ntdsdotsqlite, gMSADumper.py

## Services / ports
- [[dns]] (53), [[kerberos]] (88), [[ldap]] (389), [[smb]] (445), [[http]] (80), [[winrm]] (5985), [[rdp]] (3389)
- Windows Server 2019, Active Directory domain infiltrator.htb, Output Messenger ports 14121-14130

## Lessons / notes
- AS-REP roasting is an effective initial access vector when pre-auth is disabled
- Password reuse is a critical vulnerability in Active Directory environments
- BloodHound is essential for identifying complex ACL abuse paths
- Shadow credentials provide a stealthy alternative to password changes
- Calendar automation can be abused for persistent code execution
- Network tunneling is often required to access internal services
- Encrypted backups may contain sensitive information that requires additional processing
- BitLocker recovery keys can be extracted from backup archives
- NTDS extraction from backups provides complete credential dumps
- gMSA accounts can be compromised to extract service account credentials
- ADCS ESC4 is a powerful privilege escalation technique in domain environments
- The box demonstrates an extremely complex and realistic Active Directory compromise scenario
