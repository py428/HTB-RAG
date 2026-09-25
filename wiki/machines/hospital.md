---
type: machine
title: Hospital
platform: htb
os: mixed
difficulty: medium
tags: [windows, linux, web, ad, kerberos, php, kernel, privesc, file-upload, command-injection, password-cracking, rdp]
solved: 2026-07-09
sources: [[htb-hospital]]
related: []
---
# Hospital
> Hospital is a Windows domain controller running an Ubuntu VM with a medical company web application. The attack path involves bypassing PHP upload filters to get a webshell, exploiting kernel vulnerabilities in the Linux container, password reuse to access Windows systems, and exploiting Ghostscript via email to gain user access, with multiple paths to administrator privileges.

## Attack path
1. [[file-upload-php-bypass]] — Upload PHP webshell using .phar extension on medical records upload
2. [[disable-functions-bypass]] — Bypass PHP disable_functions using popen for RCE
3. [[kernel-exploit]] — Exploit Linux kernel with CVE-2023-35001 or GameOver(lay) for root in container
4. [[password-cracking]] — Extract and crack user hash from /etc/shadow with hashcat
5. [[password-reuse]] — Use cracked credentials to access SMB and RoundCube webmail
6. [[command-injection]] — Exploit Ghostscript via malicious EPS email attachment (CVE-2023-36664)
7. [[keystroke-capture]] — Capture admin password via Meterpreter keystroke sniffer
8. [[rdp-initial-access]] — Connect via RDP and steal admin password
9. [[xss-webshell-unintended]] — Upload webshell via XAMPP htdocs directory for NT AUTHORITY\SYSTEM

## Techniques used
- [[file-upload-php-bypass]] — Upload PHP webshell using .phar extension bypassing image upload filters
- [[disable-functions-bypass]] — Bypass PHP disable_functions using popen for full RCE
- [[kernel-exploit]] — Exploit Linux kernel vulnerability CVE-2023-35001 or GameOver(lay) for privilege escalation in container
- [[password-cracking]] — Crack Linux /etc/shadow hashes and Windows hashes using hashcat
- [[password-reuse]] — Reuse cracked credentials across different systems and services
- [[command-injection]] — Exploit Ghostscript CVE-2023-36664 via malicious EPS email attachment for code execution
- [[keystroke-capture]] — Use Meterpreter keystroke sniffer to capture admin password as typed
- [[rdp-initial-access]] - Connect via RDP to steal admin password from browser
- [[xss-webshell-unintended]] — Upload webshell to XAMPP htdocs for NT AUTHORITY\SYSTEM shell

## Tools used
- [[nmap]], [[feroxbuster]], [[ffuf]], [[hashcat]], [[weevely]], [[msfvenom]], [[evil-winrm]], [[netexec]], [[smbclient]]
- Python-based custom forward shell, proxychains, xfreerdp, kerbrute, impacket, crackmapexec, john

## Services / ports
- [[ssh]] (22), [[dns]] (53), [[kerberos]] (88), [[msrpc]] (135), [[netbios]] (139), [[http]] (443), [[smb]] (445), [[kpasswd5]] (464), [[http-rpc]] (593), [[ldap]] (636), [[ldap]] (389), [[global-catalog]] (3268), [[ldaps]] (636), [[winrm]] (5985), [[http]] (8080), [[adws]] (9389)

## Lessons / notes
- The box demonstrates a mixed OS environment with Windows host running Ubuntu VM
- PHP upload filter bypass techniques include using .phar extension among others
- Multiple kernel exploits available for privilege escalation in Linux containers
- Password reuse is a critical theme across different systems and services
- Email-based exploits can be highly effective for initial access and lateral movement
- Multiple unintended paths to administrator access demonstrate common security issues
- The box includes realistic automation with hMailServer scripting for email attachment processing
- Ghostscript exploitation requires crafting malicious EPS files with command injection payloads
