---
type: source
title: "HTB Pov writeup"
raw: raw/htb-pov.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[pov]]
---
# Source: HTB Pov writeup
> Medium HackTheBox Windows box featuring ASP.NET ViewState exploitation and SeDebugPrivilege abuse for privilege escalation.
## Key facts extracted
- dev.pov.htb subdomain hosts portfolio site with file download feature
- ViewState machine keys in web.config: validationKey (SHA1), decryptionKey (AES)
- Download feature at portfolio/contact.aspx vulnerable to path traversal with absolute paths
- sfitz has PSCredential file for alaading at C:\users\sfitz\documents\connection.xml
- alaading has SeDebugPrivilege enabled in PowerShell (disabled in cmd)
- psgetsys.ps1 exploit requires clean shell environment (WinRM, not Meterpreter)
## Filed into
[[pov]], [[directory-traversal]], [[viewstate-deserialization]], [[powershell-credential-extraction]], [[sedebugprivilege]], [[meterpreter-migrate]]
