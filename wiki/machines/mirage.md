---
type: machine
title: Mirage
platform: htb
os: windows
difficulty: hard
tags: [ad, windows, web, privesc]
solved: 2026-07-09
sources: [[htb-mirage]]
related: []
---
# Mirage

> Mirage is a Hard-level Active Directory box that starts with DNS reconnaissance and NATS service enumeration, progressing through Kerberoasting, cross-session relay attacks, and password manipulation, culminating in ESC10 certificate abuse for Domain Admin access.

## Attack path
1. Enumerate [[nfs]] shares to find incident reports revealing domain structure and missing DNS records
2. Hijack DNS for nats-svc.mirage.htb to capture [[nats]] credentials from production systems
3. Enumerate NATS service to find domain credentials for david.jjackson
4. [[kerberoasting]] to crack nathan.aadam password and gain WinRM access
5. Cross-session relay using [[remote-potato]] to obtain mark.bbond NTLM hash
6. Use mark.bbond to reset javier.mmarshall password and re-enable their account
7. Read GMSA password as javier.mmarshall to authenticate as Mirage-Service$
8. Escalate to Administrator using [[adcs]] ESC10 with shadow credential manipulation

## Techniques used
- [[dns-hijacking]] — Register nats-svc.mirage.htb A record pointing to attacker IP to capture NATS authentication credentials
- [[nats]] — Message queue system enumeration to find stored authentication logs with domain credentials
- [[kerberoasting]] — Crack nathan.aadam service ticket hash to obtain initial domain access
- [[cross-session-relay]] — Use RemotePotato0 to coerce mark.bbond authentication across sessions and capture NetNTLMv2 hash
- [[password-reset]] — Reset javier.mmarshall password using mark.bbond's ForceChangePermission privilege
- [[account-manipulation]] — Re-enable disabled javier.mmarshall account by removing ACCOUNTDISABLE flag and setting logonHours
- [[gmsa]] — Read Mirage-Service$ GMSA password as javier.mmarshall using ReadGMSAPassword permission
- [[adcs]] — ESC10 weak certificate mapping attack by manipulating mark.bbond UPN to request DC01$ certificate
- [[shadow-credentials]] — Add shadow credential to MS01$ account using LDAP shell from relayed authentication
- [[rbcd]] — Grant Mirage-Service$ RBCD privileges on DC01$ to impersonate machine account
- [[dcsync]] — Use DCSync with impersonated DC01$ ticket to dump Domain Controller hashes

## Tools used
- [[nmap]] — Port scanning and service enumeration
- [[netexec]] — SMB/LDAP enumeration and authentication testing
- [[feroxbuster]] — Directory brute force on web services
- [[nsupdate]] — DNS hijacking to register nats-svc.mirage.htb A record
- [[nats]] — NATS CLI for service enumeration and credential discovery
- [[hashcat]] — Crack Kerberos ticket hashes and NTLM hashes
- [[evil-winrm]] — WinRM shell access with Kerberos authentication
- [[bloodhound]] — Active Directory privilege analysis and attack path visualization
- [[bloodyad]] — AD account manipulation (password reset, UAC flag removal, logonHours setting)
- [[getTGT]] — Kerberos TGT request using password hashes
- [[rubeus]] — Kerberos ticket manipulation and S4U impersonation attacks
- [[certipy]] — ADCS enumeration and ESC10 exploitation
- [[ntlmrelayx]] — LDAP relay with shadow credential support
- [[runascs]] — Cross-session relay execution with RunasCs
- [[secretsdump]] — DCSync to dump NTDS.dit credential database

## Services / ports
- [[smb]] (445) — File sharing and domain authentication
- [[ldap]] (389, 636, 3268, 3269) — Directory services and domain controller operations
- [[kerberos]] (88, 464) — Kerberos authentication service
- [[nfs]] (2049) — Network file system with exposed incident reports
- [[http]] (80) — NATS web interface on port 4222
- [[winrm]] (5985) — Windows Remote Management for shell access
- [[dns]] (53) — Domain name service with dynamic update permissions
- [[rpc]] (135, 463) — Remote Procedure Call services

## Lessons / notes
- DNS records that aren't periodically refreshed can be hijacked by registering them to attacker-controlled IPs
- NATS message queue systems can store authentication credentials that may be exposed through stream enumeration
- Cross-session relay attacks enable capturing authentication from interactive desktop sessions even without process injection
- Disabled user accounts require both removing ACCOUNTDISABLE flag AND setting valid logonHours to become usable
- ESC10 attacks require controlling a victim's UPN and Schannel UPN mapping being enabled (registry key 0x4)
- GMSA passwords can be read by users with ReadGMSAPassword permission to authenticate as service accounts
- LDAP relay attacks combined with shadow credentials provide powerful persistence options even without computer creation rights
- Certificate template vulnerabilities like ESC10 can be exploited even when standard BloodHound queries don't detect them
