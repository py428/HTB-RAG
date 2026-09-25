---
type: source
title: "HTB Bruno writeup"
raw: raw/htb-bruno.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bruno]]
---
# Source: HTB Bruno writeup
> Comprehensive guide through a Windows Active Directory environment starting with FTP anonymous access, leveraging AS-REP roasting for credentials, combining ZipSlip vulnerability with DLL hijacking for initial shell, and escalating via Kerberos relay attack to achieve resource-based constrained delegation and Administrator impersonation.

## Key facts extracted
- Anonymous FTP access provided SampleScanner .NET executable source code
- AS-REP roasting successful on svc_scan user, cracked to "Sunshine1"
- ZipSlip vulnerability in .NET's Path.Combine() allowed writing outside target directory
- ProcMon identified hostfxr.dll as hijacking target in current directory
- LDAP signing not required enabled Kerberos relay attacks
- MachineAccountQuota of 10 allowed creating computer accounts for RBCD abuse
- KrbRelayUp automated DCOM coercion, relay, and RBCD configuration

## Filed into
[[bruno]], [[as-rep-roasting]], [[zipslip]], [[dll-hijacking]], [[kerberos-relay]], [[resource-based-constrained-delegation]]
