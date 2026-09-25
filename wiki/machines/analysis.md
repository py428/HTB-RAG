---
type: machine
title: Analysis
platform: htb
os: windows
difficulty: hard
tags: [ldap, php, snort, ad]
solved: 2026-07-09
sources: [[htb-analysis]]
related: []
---
# Analysis
> Windows Domain Controller with LDAP injection vulnerability in internal web application, PHP upload functionality for code execution, and Snort IDS with writable dynamic preprocessor directory leading to privilege escalation.

## Attack path
1. Subdomain enumeration → Find internal.analysis.htb
2. [[ldap-injection]] in user search → Brute force users
3. Extract password from LDAP description field → Login as technician
4. Upload [[php-webshell]] via SOC report → Shell as svc_web
5. Find autologon credentials in registry → Login as jdoe via WinRM
6. Upload malicious DLL to Snort dynamic preprocessor directory → [[dll-hijack]] → Root

## Techniques used
- [[ldap-injection]] — Wildcard injection in LDAP queries to enumerate users
- [[ldap-attribute-extraction]] — Brute force LDAP attribute values character by character
- [[ldap-description-credential]] — Password stored in LDAP description field
- [[php-webshell]] — Upload PHP script to /dashboard/uploads directory
- [[autologon-credential]] — Credentials stored in registry for auto-login
- [[dll-hijack]] — Writable Snort dynamic preprocessor directory for DLL loading

## Tools used
- [[nmap]], [[netexec]], ffuf, [[feroxbuster]], [[ldapsearch]], evil-winrm, msfvenom, icacls

## Services / ports
- [[dns]] (53), [[http]] (80, 5985), [[kerberos]] (88), [[ldap]] (389, 636, 3268, 3269), [[smb]] (445), [[mysql]] (3306), [[winrm]] (5985)

## Lessons / notes
- LDAP injection allows user enumeration and attribute extraction
- Shared service accounts often have passwords in LDAP description fields
- WinRM requires credentials in allowed users list
- Windows autologon credentials stored in HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
- Snort dynamic preprocessor directory permissions should be restricted
