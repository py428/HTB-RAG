---
type: machine
title: Authority
platform: htb
os: windows
difficulty: medium
tags: [ad, windows, ldap, privesc]
solved: 2026-07-09
sources: [[htb-authority]]
related: []
---
# Authority

> Medium Windows domain controller demonstrating ADCS exploitation paths from initial foothold through certificate-based attacks. The box showcases SMB enumeration, Ansible vault cracking, LDAP credential interception, and ESC1 certificate template abuse with computer account creation for privilege escalation.

## Attack path
1. [[nmap]] scan reveals DC with [[smb]], [[ldap]], [[kerberos]], [[http]]
2. Access Development share via guest session
3. Extract and crack Ansible vault passwords
4. Access PWM configuration manager and capture LDAP credentials
5. WinRM access as svc_ldap user
6. [[adcs]] enumeration reveals vulnerable CorpVPN template
7. Create fake computer account with ms-ds-machineaccountquota
8. Request certificate for administrator using ESC1 vulnerability
9. [[passthecert]] attack with LDAP shell or S4U2Proxy for DC compromise

## Techniques used
- [[ansible-vault-cracking]] — Ansible Vault password recovery using ansible2john and hashcat
- [[ldap-credential-capture]] — Clear-text credential interception via PWM configuration testing
- [[adcs]] — ADCS enumeration and template analysis
- [[computer-account-creation]] — MS-DS-MachineAccountQuota abuse for fake computer creation
- [[esc1]] — Certificate template enrollment allowing SAN specification
- [[passthecert]] — Certificate-based authentication to LDAP and S4U2Proxy delegation

## Tools used
- [[nmap]], [[netexec]], [[smbclient]], [[ansible-vault]], [[hashcat]], [[evil-winrm]], [[certipy]], [[impacket]], [[passthecert]]

## Services / ports
- 53/tcp — DNS (Simple DNS Plus)
- 80/tcp [[http]] — Microsoft IIS httpd 10.0
- 88/tcp [[kerberos]] — Microsoft Windows Kerberos
- 389/tcp [[ldap]] — Microsoft Windows Active Directory LDAP
- 445/tcp [[smb]] — Microsoft-ds
- 5985/tcp [[winrm]] — Microsoft HTTPAPI 2.0
- 8443/tcp [[https]] — PWM web interface

## Lessons / notes
- Ansible Vault encrypted files can be cracked with John the Ripper (mode 16900)
- PWM configuration mode can leak LDAP credentials when testing connection profiles
- ADCS ESC1 vulnerability allows any principal to enroll with arbitrary SANs
- Domain Computers enrollment requirement necessitates fake computer creation
- MachineAccountQuota attribute allows standard users to create computer accounts
- PassTheCert enables LDAP authentication when PKINIT is not properly configured
- S4U2Proxy with RBCD allows ticket impersonation for domain compromise
