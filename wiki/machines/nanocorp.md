---
type: machine
title: NanoCorp
platform: htb
os: windows
difficulty: hard
tags: [windows, ad, cve, privesc]
solved: 2026-07-09
sources: [[htb-nanocorp]]
related: []
---
# NanoCorp
> Hard-difficulty Windows Active Directory box featuring a careers portal with file upload functionality, leading to Net-NTLMv2 capture, complex AD privilege escalation, and Checkmk agent exploitation for SYSTEM.

## Attack path
1. Upload malicious ZIP file exploiting [[cve-2025-24071]] to capture Net-NTLMv2 hash
2. Crack hash to obtain credentials for service account
3. Use [[bloodhound]] to identify ACL-based privilege escalation path
4. Add user to IT_Support group and reset [[ntlm-disabled-protected-users]] account password
5. Authenticate via [[kerberos]] to bypass NTLM restrictions
6. Exploit [[cve-2024-0670]] in Checkmk agent to gain SYSTEM access

## Techniques used
- [[cve-2025-24071]] — Windows library-ms file NTLM hash leak via ZIP extraction
- [[ntlm-capture]] — Capture Net-NTLMv2 hash when Windows processes malicious library file
- [[acl-genericwrite]] — Add self to group via GenericWrite on IT_Support group
- [[ntlm-disabled-protected-users]] — ForceChangePassword on Protected Users account
- [[kerberos-authentication]] — Use Kerberos for NTLM-disabled accounts in Protected Users group  
- [[cve-2024-0670]] — Checkmk agent privilege escalation via writable temporary files

## Tools used
[[nmap]], [[feroxbuster]], [[Responder]], [[hashcat]], [[netexec]], [[bloodhound]], [[bloodyad]], [[evil-winrm-py]], [[RunasCs]]

## Services / ports
[[smb]] (445), [[ldap]] (389), [[kerberos]] (88), [[winrm]] (5986), [[http]] (80)

## Lessons / notes
- CVE-2025-24071 allows NTLM hash leak via .library-ms files extracted from ZIP archives
- Protected Users group prevents NTLM authentication but allows Kerberos
- Checkmk agent before 2.1.0p40 vulnerable to temporary file privilege escalation
- Checkmk agent creates temporary files in C:\Windows\Temp and executes them with SYSTEM privileges
- Write-protected files seeded in temp directory get executed by Checkmk repair/upgrade operations
- `msiexec /fa` (repair) triggers Checkmk agent execution flow for privilege escalation
- Automated cleanup scripts reset AD changes and temp files to maintain intended state