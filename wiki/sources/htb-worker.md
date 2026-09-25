---
type: source
title: "HTB Worker writeup"
raw: raw/htb-worker.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[worker]]
---
# Source: HTB Worker writeup
> Complete walkthrough of Worker HackTheBox machine covering Azure DevOps exploitation, SVN credential discovery, webshell upload, and pipeline abuse for privilege escalation.
## Key facts extracted
- SVN repository with historical credentials in deploy.ps1 (revision 2)
- Azure DevOps managing multiple websites with build pipelines
- Pipelines run as SYSTEM and execute commands during build process
- SVN configuration file stores plaintext passwords for multiple users
- Windows Server 2019 with IIS hosting multiple sites
- WinRM access available for Remote Management Users group
## Filed into
[[worker]], [[azure-devops-abuse]], [[svn-enumeration]], [[password-reuse]], [[winrm]], [[roguepotato]], [[windows]], [[ad]]
