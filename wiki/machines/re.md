---
type: machine
title: RE
platform: htb
os: windows
difficulty: hard
tags: [windows, web, ad, privesc, macro, xxe]
solved: 2026-07-09
sources: [[htb-re]]
related: []
---
# RE
> A reverse engineer's box running Windows with a malware sandbox that processes uploaded documents. The attack path involves uploading a malicious .ods file with obfuscated macro, exploiting a WinRar ACE vulnerability to write a webshell, then using Ghidra project XXE to obtain credentials for WinRM access.

## Attack path
1. [[nmap]] enumeration to find open [[smb]] and [[http]] ports
2. [[smb]] malware_dropbox upload for malicious .ods file with obfuscated macro
3. [[macro-obfuscation]] using Invoke-Obfuscation to bypass Yara rules
4. [[winrar-slip]] vulnerability to write webshell via ACE archive
5. [[xxe]] in Ghidra project files to capture NetNTLM hash with [[responder]]
6. [[hashcat]] to crack credentials for [[winrm]] access
7. Unintended paths via UsoSvc service abuse or DiagHub ZipSlip to SYSTEM

## Techniques used
- [[macro-obfuscation]] — Bypass Yara-based malware detection using Invoke-Obfuscation
- [[winrar-slip]] — ACE archive path traversal to write webshell outside intended directory
- [[xxe]] — External entity injection in Ghidra .prp files to trigger SMB authentication
- [[dnsadmins-dnscmd-abuse]] — Load malicious DLL via dnscmd to get SYSTEM
- [[service-permission-abuse]] — Modify UsoSvc service binary path for privilege escalation

## Tools used
[[nmap]] | [[smbclient]] | [[hashcat]] | [[evil-winrm]] | [[impacket]] | [[mimikatz]] | [[responder]] | chisel | accesschk

## Services / ports
[[smb]] (445) | [[http]] (80) | [[winrm]] (5985)

## Lessons / notes
- Malware sandbox processing requires obfuscation to avoid detection
- WinRar ACE vulnerability allows writing files outside extraction directory
- Ghidra project XML files are vulnerable to XXE attacks
- DnsAdmins can load arbitrary DLLs via dnscmd for privilege escalation
- PowerShell transcripts may contain sensitive command history
- EFS encryption requires specific user certificates for file access
- Chisel tunneling needed when WinRM is firewalled
