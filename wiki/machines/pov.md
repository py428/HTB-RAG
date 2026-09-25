---
type: machine
title: Pov
platform: htb
os: windows
difficulty: medium
tags: [windows, web, privesc, ad]
solved: 2026-07-09
sources: [[htb-pov]]
related: []
---
# Pov
> Medium Windows box with ASP.NET file read vulnerability, ViewState deserialization using ysoserial.net for initial access, PowerShell credential pivot, and SeDebugPrivilege abuse via psgetsys.ps1 or Meterpreter migrate for system.
## Attack path
1. [[directory-traversal]] — Read arbitrary files via path parameter in download feature (regex bypass with absolute paths)
2. [[viewstate-deserialization]] — Use ysoserial.net with AES/SHA1 machine keys from web.config for RCE
3. [[powershell-credential-extraction]] — Extract alaading password from PSCredential in connection.xml
4. [[sedebugprivilege]] — Abuse SeDebugPrivilege via psgetsys.ps1 or Meterpreter migrate to get SYSTEM
## Techniques used
- [[directory-traversal]] — Bypass ../ regex with absolute paths to read files like C:\windows\win.ini
- [[viewstate-deserialization]] — ysoserial.net ViewState plugin with WindowsIdentity gadget
- [[powershell-credential-extraction]] — Import-CliXml to decrypt PSCredential password
- [[sedebugprivilege]] — Debug programs privilege allows code injection into SYSTEM processes
- [[meterpreter-migrate]] — Migrate Meterpreter session into winlogon.exe running as SYSTEM
## Tools used
- [[nmap]] — Port scanning (HTTP 80 only)
- [[ffuf]] — Subdomain brute force (finds dev.pov.htb)
- [[feroxbuster]] — Directory brute force
- [[ysoserial.net]] — Generate ViewState deserialization payload
- [[curl]] — HTTP requests with tcpdump for ICMP verification
- [[netcat]] — Reverse shell listener
- [[runascs]] — Run processes as alaading user
- [[meterpreter]] — Shell as alaading with migrate capability
- [[chisel]] — Port forwarding for WinRM access
- [[evil-winrm]] — WinRM shell connection
## Services / ports
- [[http]] — TCP 80 (IIS 10.0, ASP.NET)
## Lessons / notes
- ASP.NET ViewState requires machine validationKey and decryptionKey from web.config
- Path parameter vulnerable to regex bypass ../ with absolute paths (C:\inetpub\...)
- PSCredential files encrypted with DPAPI, can only be decrypted on the host
- SeDebugPrivilege in cmd vs PowerShell: disabled in cmd, enabled in PowerShell
- psgetsys.ps1 ImpersonateFromParentPid fails from Meterpreter, works from WinRM
- Error 122 (ERROR_INSUFFICIENT_BUFFER) from psgetsys indicates shell incompatibility
