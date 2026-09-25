---
type: machine
title: Hathor
platform: htb
os: windows
difficulty: insane
tags: [windows, ad, web, code-signing, kerberos, dcsync]
solved: 2026-07-09
sources: [[htb-hathor]]
related: []
---
# Hathor
> Insane difficulty Windows domain controller with mojoPortal CMS exploitation, DLL hijacking via AppLocker whitelist, code signing certificate abuse from recycled bin, and DCSync for domain admin credentials.

## Attack path
1. Default mojoPortal admin credentials for web shell upload
2. [[dll-hijacking]] via SMB share with AutoIt script loading 7-zip64.dll
3. Code signing certificate extraction from recycle bin with [[crackpkcs12]]
4. [[code-signing]] to hijack Get-bADpasswords script execution as bpassrunner
5. [[dcsync]] with Get-ADReplAccount for admin NT hash
6. [[kerberos]] golden ticket from NTLM hash for administrator shell

## Techniques used
- [[webshell]] — ASPX webshell upload via mojoPortal file manager with extension change blocked, using copy/rename to bypass
- [[dll-hijacking]] — Overwriting whitelisted DLL (7-zip64.dll) in SMB share loaded by scheduled AutoIt script for execution as GinaWild
- [[applocker]] — Windows application whitelisting blocks unsigned binaries but allows whitelisted paths and signed binaries
- [[code-signing]] — Abusing code signing certificate found in recycle bin to sign malicious PowerShell script
- [[crackpkcs12]] — Brute-forcing PKCS12 certificate password to extract private key for code signing
- [[dcsync]] — Using Get-ADReplAccount as privileged user to dump domain controller password hashes
- [[kerberos]] — Creating golden ticket from NTLM hash using ktutil or Impacket getTGT.py

## Tools used
- [[nmap]]
- [[crackmapexec]]
- [[smbclient]]
- [[openssl]]
- crackpkcs12
- Visual Studio
- evil-winrm
- [[impacket]]
- ktutil
- kinit

## Services / ports
- [[dns]] (53)
- [[http]] (80)
- [[kerberos]] (88)
- [[smb]] (445)
- [[ldap]] (389, 636, 3268, 3269)
- [[winrm]] (5985)

## Lessons / notes
- mojoPortal default credentials (admin@admin.com/admin) are publicly documented
- AppLocker can whitelist specific DLL paths for execution even when unsigned
- Scheduled tasks running whitelisted binaries can be exploited via DLL hijacking
- Recycle bin may contain code signing certificates with weak passwords
- Code signing certificates can be used to bypass AppLocker script restrictions
- Protected Users group disables NTLM authentication, requiring Kerberos for domain access
- DCSync requires Domain Admin privileges or delegated replication rights
- Golden tickets can be created from NTLM hashes using Kerberos tools
