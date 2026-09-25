---
type: machine
title: Jab
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, kerberos, xmpp, web, privesc]
solved: 2026-07-09
sources: [[htb-jab]]
related: []
---
# Jab
> Windows domain controller with an XMPP/Jabber server. Initial access via AS-REP roasting on users discovered through the Jabber service, then DCOM abuse for execution, and finally OpenFire plugin upload for SYSTEM.

## Attack path
1. [[as-rep-roasting]] to crack user password via XMPP-enumerated users
2. Password reuse found in private XMPP chat room
3. [[dcom-abuse]] via MMC20 for shell as svc_openfire
4. Port forwarding to access OpenFire admin panel
5. Malicious OpenFire plugin upload for SYSTEM

## Techniques used
- [[as-rep-roasting]] — Enumerated 2684 users via Pidgin XMPP client, found 3 with preauth disabled, cracked jmontgomery password
- [[dcom-abuse]] — Used Impacket's dcomexec.py with MMC20 object for command execution
- openfire-plugin-abuse — Uploaded malicious plugin via admin panel for SYSTEM execution

## Tools used
[[nmap]], [[netexec]], pidgin, GetNPUsers.py, [[hashcat]], bloodhound-python, dcomexec.py, [[chisel]]

## Services / ports
[[kerberos]] (88), [[ldap]] (389/636/3268/3269), xmpp (5222/5223/5262/5263/5269/5270/5275/5276), [[winrm]] (5985), [[smb]] (445), [[http]] (80/7070/7443)

## Lessons / notes
- XMPP services can provide extensive user enumeration through directory search features
- OpenFire admin panels listening on localhost can be accessed via port forwarding
- CVE-2023-32315 demonstrates OpenFire plugin upload vulnerability
- DCOM MMC20 abuse works well when users have "First Degree DCOM Privileges"
