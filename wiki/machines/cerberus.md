---
type: machine
title: Cerberus
platform: htb
os: windows
difficulty: hard
tags: [windows, linux, ad, container, icinga, firejail, winrm, manage-engine, privesc]
solved: 2026-07-09
sources: [[htb-cerberus]]
related: []
---
# Cerberus
> Cerberus is unique in that it's a Windows host running an Ubuntu VM with Icinga. I'll exploit CVE-2022-24716 to read Icinga config files for credentials, then CVE-2022-24715 to write a malicious module and get RCE in the container. From there, I'll exploit Firejail for container root, extract SSSD credentials to access the Windows host via WinRM, and exploit ManageEngine ADSelfService Plus for SYSTEM.

## Attack path
1. Exploit [[icinga-cve-2022-24716]] to leak matthew credentials
2. Exploit [[icinga-cve-2022-24715]] for arbitrary file write of PHP webshell module
3. Get shell in container, exploit [[firejail-cve-2022-31214]] for container root
4. Extract matthew hash from [[sssd-cache]]
5. Tunnel through VM with [[chisel]] to access [[winrm]] on host
6. Find ManageEngine ADSelfService Plus backup with [[saml-cve]] for SYSTEM

## Techniques used
- [[icinga-cve-2022-24716]] — Arbitrary file disclosure via empty asset path in StaticController
- [[icinga-cve-2022-24715]] — Arbitrary file write via path traversal in SSH Identity username field
- [[firejail-cve-2022-31214]] — Escape Firejail sandbox via --join technique
- [[sssd-cache]] — Extract cached passwords from SSSD database cache_cerberus.local.ldb
- [[chisel]] — Reverse tunnel through VM to access host services
- [[saml-cve]] — SAML vulnerability in ManageEngine ADSelfService Plus for authentication bypass

## Tools used
- [[nmap]]
- [[dig]]
- [[curl]]
- ssh-keygen
- chisel
- hashcat
- [[evil-winrm]]
- smbserver.py
- 7z

## Services / ports
- [[ssh]] (22)
- [[http]] (8080)
- [[dns]] (UDP 53)
- [[ntp]] (UDP 123)
- [[ldap]] (UDP 389)
- [[winrm]] (5985)

## Lessons / notes
- Windows host running Ubuntu VM (172.16.22.2 → 172.16.22.1)
- IcingaWeb2 version 2.9.x with path traversal vulnerabilities
- Config files leak matthew/IcingaWebPassword2023 credentials
- Module path change to /dev allows writable module location
- Firejail sandbox escape via /proc/[pid]/root mount
- SSSD contains cached password hash for matthew (147258369)
- ManageEngine ADSelfService Plus with backup .ezip file
- SAML authentication bypass leads to aris/HTB_@dm1n!d credentials
