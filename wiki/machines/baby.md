---
type: machine
title: Baby
platform: htb
os: windows
difficulty: easy
tags: [ad, windows, ldap, privesc]
solved: 2026-07-09
sources: [[htb-baby]]
related: []
---
# Baby
> Baby is an easy Windows Active Directory box where anonymous LDAP binding reveals user information, password spraying finds valid credentials, and Backup Operator privileges allow dumping credentials for privilege escalation.

## Attack path
1. [[ldap-enumeration]] via anonymous binding to find default credential
2. [[password-spray]] to find additional working credentials
3. [[backup-operator-abuse]] with SeBackupPrivilege to dump local hashes
4. [[credential-dumping]] to obtain Administrator password
5. [[pth]] to gain administrative access

## Techniques used
- [[ldap-enumeration]] — Anonymous LDAP binding reveals all domain users and attributes
- [[password-spray]] — Default credentials tested against all users to find additional matches
- [[backup-operator-abuse]] — SeBackupPrivilege allows copying sensitive files including SAM database
- [[credential-dumping]] — Using secretsdump to extract hashes from local and domain databases
- [[pth]] — Pass-the-hash attack using NTLM hash for Administrator access

## Tools used
[[nmap]], [[netexec]], [[ldapsearch]], [[impacket]], [[evil-winrm]]

## Services / ports
[[smb]] (445), [[ldap]] (389), [[kerberos]] (88), [[dns]] (53)

## Lessons / notes
- Always check for anonymous LDAP binding on domain controllers
- Default credentials are worth testing in AD environments
- Backup Operators group has powerful privileges for credential extraction
- Local Administrator credentials may be reused across the domain
- Pass-the-hash is often sufficient for administrative access
