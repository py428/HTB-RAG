---
type: machine
title: Axlle
platform: htb
os: windows
difficulty: hard
tags: [ad, windows, phishing, privesc]
solved: 2026-07-09
sources: [[htb-axlle]]
related: []
---
# Axlle
> Axlle is a hard Windows Active Directory box featuring Excel XLL add-on phishing for initial access, followed by credential harvesting and LOLBIN abuse for privilege escalation.

## Attack path
1. [[xll-phishing]] via malicious Excel add-on file sent to accounts@axlle.htb
2. [[url-file-exploit]] to gain reverse shell as gideon.hamill
3. [[credential-harvesting]] to find hardcoded credentials
4. [[password-change]] to compromise dallon.matrix account
5. [[lolbin-abuse]] using StandaloneRunner.exe for privilege escalation

## Techniques used
- [[xll-phishing]] — Excel XLL add-on files execute code automatically when opened, bypassing macro restrictions
- [[url-file-exploit]] — URL files can execute arbitrary commands when opened
- [[credential-harvesting]] — Hardcoded credentials found in application files and configuration
- [[password-change]] — Password change functionality abused to take over accounts
- [[lolbin-abuse]] — StandaloneRunner.exe used to execute commands with higher privileges

## Tools used
[[nmap]], [[swaks]], [[feroxbuster]], [[netexec]], [[evil-winrm]]

## Services / ports
[[smtp]] (25), [[http]] (80), [[smb]] (445), [[ldap]] (389), [[kerberos]] (88), [[winrm]] (5985), [[rdp]] (3389)

## Lessons / notes
- XLL phishing represents a modern alternative to macro-based phishing
- URL files can be used for initial access when direct execution is blocked
- Look for credentials in non-obvious locations like application configurations
- LOLBINs (Living Off The Land Binaries) are useful for privilege escalation
- Password change functionality can sometimes be abused without knowing current password
