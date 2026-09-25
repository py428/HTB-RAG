---
type: machine
title: "HTB Phantom"
platform: htb
os: windows
difficulty: medium
tags: [ad, windows, privesc]
solved: 2026-07-09
sources: [[htb-phantom]]
related: []
---
# HTB Phantom
> Windows Domain Controller exploitation starting with guest SMB access, password spraying with leaked credentials, VeraCrypt volume cracking, and BloodHound-guided RBCD abuse without computer object quota.

## Attack path
1. Enumerate [[domain-controller]] with [[nmap]] and [[netexec]]
2. Access [[smb]] share as guest, find default password in email attachment
3. Perform [[rid-cycle]] attack to enumerate domain users
4. [[password-spray]] with leaked default password to find ibryant user
5. Access Departments share, find VeraCrypt volume with VyOS backup
6. Crack [[veracrypt-cracking]] volume with custom wordlist and hashcat rules
7. Extract svc_sspr credentials from VyOS config, authenticate to domain
8. Analyze domain with [[bloodhound]] to identify attack paths
9. Use [[rbcd]] (AllowedToAct) with SPN-less technique via password hash manipulation
10. Perform DCSync to dump Administrator credentials and get root shell

## Techniques used
- [[smb-guest-access]] — Access public share with guest account for initial file access
- [[rid-cycle]] — Enumerate domain users via SMB RID brute forcing as guest
- [[password-spray]] — Test default password across multiple domain users
- [[veracrypt-cracking]] — Custom wordlist generation based on company name + year + special chars
- [[bloodhound]] — Identify shortest path to Tier Zero and delegation abuse opportunities
- [[rbcd]] — Resource-based constrained delegation without computer object quota using SPN-less technique

## Tools used
- [[nmap]] — Port scanning and DC service identification
- [[netexec]] — SMB/LDAP enumeration, password spraying, BloodHound data collection
- [[kerbrute]] — Fast password spraying against Kerberos
- [[hashcat]] — VeraCrypt volume cracking with custom rules
- veracrypt — Volume mounting and file extraction
- [[bloodhound]] — Attack path analysis and delegation identification
- impacket — RBCD exploitation with rbcd.py, getTGT.py, changepasswd.py, getST.py

## Services / ports
- [[domain-controller]] — Windows Server 2022 with phantom.vl domain
- [[smb]] (445) — File sharing with guest access enabled
- [[ldap]] (389, 3268, 3269) — Directory services
- [[kerberos]] (88, 464) — Authentication services
- [[winrm]] (5985) — Remote management
- [[rdp]] (3389) — Remote desktop

## Lessons / notes
- Default password format: CompanyName + Year + Special Character (e.g., Phantom2025!)
- Custom hashcat rules effective for pattern-based passwords
- MachineAccountQuota set to 0 prevents standard RBCD with computer creation
- SPN-less RBCD technique works by setting user password hash to match TGT session key
- ForceChangePassword privilege allows resetting other users' passwords
- AllowedToAct attribute enables RBCD without standard delegation setup
- VyOS configuration files may contain plaintext credentials for VPN users
