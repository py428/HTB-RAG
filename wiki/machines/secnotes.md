---
type: machine
title: SecNotes
platform: htb
os: windows
difficulty: medium
tags: [web, ad, windows, xsrf, sqli]
solved: 2026-07-09
sources: [[htb-secnotes]]
related: []
---
# SecNotes
> SecNotes is a medium Windows box featuring a PHP note-taking application with both XSRF and second-order SQL injection vulnerabilities. The intended path uses XSRF to change the admin password via a contact form that an admin bot visits, while an unintended path skips this via second-order SQL injection. After obtaining SMB credentials, a webshell is uploaded through an SMB share, and privilege escalation involves extracting credentials from the Windows Subsystem for Linux (WSL) bash history.

## Attack path
1. [[nmap]] enumeration reveals HTTP and SMB services
2. Register account on SecNotes web application and explore functionality
3. Discover [[xsrf]] vulnerability - change password form accepts GET requests and doesn't require current password
4. Exploit XSRF via contact form - admin bot visits submitted URLs, changing Tyler's password
5. Access Tyler's account and find SMB credentials in saved notes
6. Upload PHP webshell to SMB share and execute via IIS on port 8808
7. Upload nc.exe via SMB and execute reverse shell for user access
8. Enumerate WSL installation and find bash.exe - access Linux subsystem from Windows
9. Extract administrator credentials from .bash_history in WSL filesystem
10. Use [[winexe]] or [[psexec]] with admin credentials for shell and root.txt

## Techniques used
- [[xsrf]] — Password change form accepts GET requests without CSRF protection or current password
- [[second-order-sqli]] — Registration with SQLi username (' or 1='1) allows viewing all users' notes
- [[smb-webshell-upload]] — Upload PHP webshell via SMB share for execution through IIS
- [[wsl-credential-extraction]] — Access Linux subsystem to extract Windows admin credentials from bash history

## Tools used
[[nmap]], [[gobuster]], [[smbmap]], [[smbclient]], [[netcat]], [[winexe]]

## Services / ports
80/tcp — HTTP (IIS/PHP), 445/tcp — SMB, 8808/tcp — HTTP (IIS)

## Lessons / notes
- XSRF can be exploited when forms don't require POST or current password verification
- Contact forms that visit URLs provide XSRF exploitation vectors
- Second-order SQL injection occurs when stored data is used in subsequent queries without sanitization
- WSL bash history can contain Windows credentials in clear text
- SMB shares mapped to web directories allow direct webshell upload
