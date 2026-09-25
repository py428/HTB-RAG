---
type: machine
title: Bruno
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, ftp, zipslip, dll-hijacking, kerberos, delegation, privesc]
solved: 2026-07-09
sources: [[htb-bruno]]
related: []
---
# Bruno
> Windows Active Directory box featuring a .NET malware scanning service with ZipSlip vulnerability and DLL hijacking opportunity. Initial access through AS-REP roasting, then combining file upload vulnerabilities with DLL hijacking to get code execution as a service account. Privilege escalation via Kerberos relay attack exploiting lack of LDAP signing to achieve resource-based constrained delegation and impersonate Administrator.

## Attack path
1. [[as-rep-roasting]] — Crack svc_scan AS-REP hash to get initial credentials
2. [[zipslip]] — Abuse ZipSlip in .NET SampleScanner to write malicious DLL via SMB
3. [[dll-hijacking]] — Plant hostfxr.dll loaded by SampleScanner.exe for reverse shell
4. [[kerberos-relay]] — Relay SYSTEM authentication via KrbRelayUp to configure RBCD
5. [[resource-based-constrained-delegation]] — Impersonate Administrator using S4U2Self/S4U2Proxy

## Techniques used
- [[as-rep-roasting]] — AS-REP roasting against svc_scan user to crackable hash
- [[zipslip]] — .NET ZipFile vulnerability using absolute paths and path traversal in archive entries
- [[dll-hijacking]] — Load order hijacking of hostfxr.dll in current directory
- [[kerberos-relay]] — KrbRelayUp to relay SYSTEM authentication to LDAP for RBCD configuration
- [[resource-based-constrained-delegation]] — RBCD abuse with getST.py for Administrator impersonation

## Tools used
[[nmap]], [[ffuf]], [[feroxbuster]], [[smbclient]], [[netexec]], [[kerbrute]], hashcat, msfvenom, [[chisel]], python, KrbRelayUp, [[impacket]]

## Services / ports
[[ftp]] (21), [[http]] (80 - IIS/ASP.NET), [[dns]] (53), [[kerberos]] (88), [[ldap]] (389,636,3268,3269), [[smb]] (445), [[rpc]] (135)

## Lessons / notes
- FTP anonymous access provided .NET SampleScanner source code analysis
- AS-REP roasting worked on svc_scan user without pre-authentication
- ZipSlip vulnerability in .NET ZipFile.ExtractToFile() using absolute paths
- ProcMon analysis identified DLL hijacking opportunities with NAME NOT FOUND results
- LDAP signing not required enabled Kerberos relay attacks
- MachineAccountQuota of 10 allowed creating computer accounts for delegation abuse
- KrbRelayUp automates DCOM coercion, relay, and RBCD configuration in one tool
