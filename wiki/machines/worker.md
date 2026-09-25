---
type: machine
title: Worker
platform: htb
os: windows
difficulty: medium
tags: [windows, web, ad, privesc]
solved: 2026-07-09
sources: [[htb-worker]]
related: []
---
# Worker
> Azure DevOps environment with multiple websites and SVN repository. Initial access through credentials found in SVN history, then upload ASPX webshell via Azure DevOps pipelines. Privilege escalation involves Azure DevOps pipeline abuse to get SYSTEM shell, with RoguePotato as alternative privesc path.
## Attack path
1. Find credentials in SVN repository history to access Azure DevOps as nathen
2. Upload ASPX webshell via Azure DevOps by creating branch and triggering pipeline build
3. Find more credentials in SVN config files to access as robisl via WinRM
4. Create Azure DevOps pipeline as robisl to get shell as SYSTEM
## Techniques used
- [[svn-enumeration]] — Historical SVN commits containing plaintext credentials in deployment scripts
- [[azure-devops-abuse]] — Pipeline abuse to upload webshells and gain SYSTEM execution
- [[password-reuse]] — SVN credentials reused for Windows authentication
- [[winrm]] — Remote shell access using credentials from SVN configuration
- [[roguepotato]] — SeImpersonatePrivilege exploitation for SYSTEM access
## Tools used
- [[nmap]], [[svn]], [[smbclient]], [[evil-winrm]], [[netcat]], [[chisel]], roguepotato
## Services / ports
- [[http]] (80), SVN (3690), [[winrm]] (5985)
## Lessons / notes
- Azure DevOps pipelines run as SYSTEM and can execute arbitrary commands
- Branch protection can be bypassed by creating non-master branches
- SVN stores plaintext passwords in configuration files
- RoguePotato exploits SeImpersonatePrivilege on Windows Server 2019+
- Chisel tunneling needed for RoguePotato when firewall blocks inbound connections
