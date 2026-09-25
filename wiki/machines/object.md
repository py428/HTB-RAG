---
type: machine
title: Object
platform: htb
os: windows
difficulty: hard
tags: [windows, ad, jenkins, winrm, bloodhound, acl-abuse, kerberoasting, logon-script, privesc]
solved: 2026-07-09
sources: [[htb-object]]
related: []
---

# Object
> Object is an Active Directory environment with Jenkins automation server, requiring credential extraction, BloodHound analysis for ACL abuse paths, and multiple privilege escalation techniques via logon scripts and group ownership.

## Attack path
1. Create Jenkins job and trigger via schedule or remote API token
2. [[jenkins-credential-decryption]] — Extract encrypted password from Jenkins config.xml
3. [[winrm]] — Access as oliver via decrypted credentials
4. [[bloodhound]] — Analyze AD for privilege escalation paths
5. [[acl-genericwrite]] — ForceChangePassword on smith from oliver
6. [[logon-script-abuse]] — Set maria's scriptPath to execute commands as maria
7. [[acl-writeowner]] — maria can take ownership of Domain Admins group
8. Add maria to Domain Admins for root access

## Techniques used
- [[jenkins-rce]] — Create jobs with batch commands, trigger via schedule or API
- [[jenkins-credential-decryption]] — Decrypt Jenkins credentials with master.key and hudson.util.Secret
- [[firewall-enumeration]] — Identify outbound TCP block via Get-NetFirewallRule
- [[bloodhound]] — AD analysis shows ACL abuse paths
- [[acl-genericwrite]] — Set-DomainObject to modify logon script path
- [[forcechangepassword]] — Set-DomainUserPassword with ForceChangePassword privilege
- [[kerberoasting]] — Add SPN with Set-DomainObject and request TGT with Get-DomainSPNTicket
- [[logon-script-abuse]] — Automated task runs maria's logon script repeatedly
- [[acl-writeowner]] — Set-DomainObjectOwner to take group ownership
- [[dacl-write-members]] — Add-DomainGroupMember after granting full rights

## Tools used
- [[nmap]]
- Jenkins (create jobs, API tokens)
- jenkins-credentials-decryptor
- [[evil-winrm]]
- SharpHound/PowerView
- [[bloodhound]]
- crackmapexec
- [[kerberoast]] tools (Get-DomainSPNTicket)

## Services / ports
- HTTP (80) — IIS 10.0
- WinRM (5985) — HTTPAPI 2.0
- HTTP (8080) — Jenkins/Jetty 9.4.43
- DNS (53)
- Kerberos (88)
- LDAP (389)
- SMB (445)

## Lessons / notes
- Jenkins jobs can be triggered via cron-like schedules or authenticated API calls
- Jenkins credentials stored encrypted in users/*/config.xml files
- Firewall can block all outbound TCP but allow ICMP for exfiltration
- BloodHound essential for AD privilege escalation path analysis
- ForceChangePassword allows password changes without knowing current password
- Logon scripts execute repeatedly when set via scriptPath attribute
- WriteOwner on group allows taking ownership and granting full permissions
- Add-DomainObjectAcl grants rights, Add-DomainGroupMember adds to group
- Domain Admin membership provides full administrative access
- SharpHound.ps1 (deprecated) works when SharpHound.exe fails authentication
