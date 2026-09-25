---
type: machine
title: StreamIO
platform: htb
os: windows
difficulty: medium
tags: [windows, ad, web, privesc, sqli, rfi, firefox-credentials, bloodhound, laps]
solved: 2026-07-09
sources: [[htb-streamio]]
related: []
---
# StreamIO
> Windows domain controller with PHP/IIS web application vulnerable to SQL injection and file inclusion, requiring Firefox credential extraction and BloodHound/LAPS exploitation for administrator access.
## Attack path
1. [[sqli]] in watch.streamio.htb search to dump database and crack hashes
2. Login as admin, find debug parameter to leak master.php source
3. [[rfi]] via file include in master.php for RCE as yoshihide
4. [[firefox-credentials]] extraction to find JDgodd domain credentials
5. [[bloodhound]] analysis to find Core Staff group path to LAPS
6. [[laps]] read ms-MCS-AdmPwd to get administrator password
## Techniques used
- [[sqli]] — Union-based injection with comment truncation ("';-- -") bypassing WAF
- [[file-include]] — Remote file inclusion via eval(file_get_contents()) in debug parameter
- [[firefox-credentials]] — Firepwd to decrypt saved passwords from key4.db and logins.json
- [[bloodhound]] — AD analysis to find Core Staff ownership and LAPS read rights
- [[laps]] — Read local administrator password from ms-MCS-AdmPwd attribute
## Tools used
- [[nmap]] — full port scan and domain controller identification
- feroxbuster — directory brute force with .php extension
- wfuzz — parameter fuzzing to find debug endpoint
- [[hashcat]] — MD5 hash cracking with rockyou.txt
- [[hydra]] — web login brute force
- evil-winrm — WinRM shell access
- Firepwd — Firefox password decryption
- bloodhound-python — AD data collection
- [[ldapsearch]] — LAPS password retrieval
- PowerView — AD group manipulation
## Services / ports
- [[dns]] (53) — Domain DNS service
- [[kerberos]] (88) — Windows domain authentication
- [[ldap]] (389, 3268, 636, 3269) — Active Directory services
- [[http]] (80, 443) — IIS with PHP applications
- [[smb]] (445) — Domain controller file sharing
- [[winrm]] (5985) — Windows Remote Management
## Lessons / notes
- MSSQL comment-based injection ("';-- -") bypasses basic filters
- PHP file inclusion with eval() is equivalent to code execution
- Firefox stores credentials encrypted in key4.db and logins.json files
- LAPS extends AD with local administrator password management
- BloodHound essential for AD privilege escalation path analysis
- Core Staff group often has LAPS read permissions in domain environments
