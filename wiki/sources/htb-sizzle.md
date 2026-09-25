---
type: source
title: "HTB Sizzle writeup"
raw: raw/htb-sizzle.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[sizzle]]
---
# Source: HTB Sizzle writeup
> Detailed Windows Active Directory exploitation guide covering SMB SCF file hash capture, certificate-based WinRM authentication, Kerberoasting, AppLocker bypasses, and DCSync attacks, plus unintended paths and Burp Suite NTLM authentication issues.

## Key facts extracted
- Department Shares SMB share with write access to Users/Public and ZZ_ARCHIVE directories
- Active Directory Certificate Services (AD CS) running with /certsrv and /certenroll endpoints
- mrlky user has http/sizzle SPN and GetChanges/GetChangesAll privileges for DCSync
- AppLocker restricting execution to Windows folder and Program Files, CLM in effect
- Unintended paths: clean.bat file modification in administrator documents, NTLM hashes exposed in file.txt

## Filed into
[[sizzle]], [[ntlm-capture-via-scf]], [[ad-cs-certificate-auth]], [[kerberoasting]], [[dcsync]], [[applocker-bypass]]