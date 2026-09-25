---
type: machine
title: Delegate
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, kerberos, delegation, dcsync, privesc]
solved: 2026-07-09
sources: [[htb-delegate]]
related: []
---

# Delegate

> Windows Domain Controller where credentials leaked via SMB share lead to Kerberoasting, delegation abuse, and ultimately DCSync for Domain Admin access.

## Attack path

1. Enumerate [[smb]] with null session to find `users.bat` script containing credentials
2. Use leaked credentials to authenticate and perform [[kerberoasting]] against target user
3. Crack Kerberos ticket to get shell access via [[winrm]]
4. Abuse `SeEnableDelegationPrivilege` to create machine account with [[unconstrained-delegation]]
5. Coerce authentication from DC to capture machine account TGT
6. Perform [[dcsync]] dump to get Administrator hash and root shell

## Techniques used

- [[smb]] — Anonymous SMB access reveals scripts with hardcoded credentials
- [[kerberoasting]] — Targeted Kerberoast using `GenericWrite` privilege to add SPN and crack hash
- [[unconstrained-delegation]] — Abuse machine account with delegation enabled to capture DC TGT
- [[dcsync]] — Use DC machine account TGT to dump all domain hashes including Administrator

## Tools used

- [[netexec]] — SMB enumeration, authentication, and DCSync
- [[smbclient]] — Access SYSVOL share to retrieve credential-leaking scripts
- targetedKerberoast.py — Automated Kerberoasting with SPN manipulation
- [[hashcat]] — Crack Kerberos TGS hash
- evil-winrm-py — WinRM shell access
- addcomputer.py (Impacket) — Create fake machine account
- krbrelayx — Set up unconstrained delegation relay
- BloodyAD — Configure delegation on machine account
- [[curl]] — Coerce authentication via PrinterBug

## Services / ports

- [[smb]] (445) — Anonymous access to SYSVOL with credential-leaking scripts
- [[kerberos]] (88) — Kerberos authentication service
- [[ldap]] (389, 636) — Domain controller services
- [[winrm]] (5985) — Remote shell access
- [[dns]] (53) — Domain DNS services
- [[http]] (47001) — WinRM HTTP endpoint

## Lessons / notes

- Always check SYSVOL scripts for credential leaks - `users.bat` contained domain credentials
- Targeted Kerberoasting is powerful when you have `GenericWrite` over a user - add SPN, roast, clean up
- `SeEnableDelegationPrivilege` with MachineAccountQuota > 0 enables unconstrained delegation abuse
- KrbRelayUp / unconstrained delegation allows capturing DC TGT for DCSync
- Multiple coercion methods available (PrinterBug, PetitPotam, DFSCoerce) - test which works
- DC machine account TGT is equivalent to DA for DCSync purposes