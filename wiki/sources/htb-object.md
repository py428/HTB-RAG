---
type: source
title: "HTB Object writeup"
raw: raw/htb-object.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[object]]
---

# Source: HTB Object writeup
> Comprehensive AD exploitation guide covering Jenkins credential theft, WinRM access, BloodHound analysis, ACL abuse for privilege escalation, and multiple paths to Domain Admin.

## Key facts extracted
- Jenkins creates scheduled tasks or remote API triggers for job execution
- Credentials encrypted with master.key and hudson.util.Secret in Jenkins secrets
- Firewall rule "BlockOutboundDC" blocks all outbound TCP but allows ICMP
- oliver has ForceChangePassword on smith user
- smith has GenericWrite on maria user
- maria has WriteOwner on Domain Admins group
- Scheduled task "RunLogOn" executes maria's logon script repeatedly as maria
- maria's logon script path points to C:\programdata\cmd.ps1
- SharpHound.exe fails auth, SharpHound.ps1 (deprecated) works
- Multiple escalation paths: kerberoasting, password change, logon scripts

## Filed into
[[object]], [[jenkins-rce]], [[jenkins-credential-decryption]], [[firewall-enumeration]], [[bloodhound]], [[acl-genericwrite]], [[forcechangepassword]], [[kerberoasting]], [[logon-script-abuse]], [[acl-writeowner]], [[dacl-write-members]]
