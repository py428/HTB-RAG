---
type: machine
title: "HTB Pterodactyl"
platform: htb
os: linux
difficulty: medium
tags: [linux, web, ad, ldap, windows, kerberos, privesc, php]
solved: 2026-07-09
sources: [[htb-pterodactyl]]
related: []
---

# HTB Pterodactyl

> Pterodactyl hosts a Minecraft community site alongside an instance of the Pterodactyl game-server management panel. I'll exploit an unauthenticated directory traversal in the panel's locale endpoint that gets PHP to include arbitrary files on disk, and chain it with the classic PEAR pearcmd technique to write and execute a webshell. From there I'll read database credentials, crack a bcrypt hash, and pivot to a user who reuses that password. The box runs openSUSE, where I'll abuse a PAM environment-variable flaw to convince Polkit I'm a local console session, then exploit a libblockdev/udisks vulnerability to mount a crafted XFS image carrying a SetUID-root shell and escalate to root.

## Attack path

1. [[directory-traversal]] for file inclusion via Pterodactyl Panel locale endpoint
2. [[lfi-to-rce]] via PEAR pearcmd.php technique to write webshell
3. [[credential-extraction]] from database config files
4. [[hash-cracking]] bcrypt hash for user pivot
5. [[password-reuse]] to escalate to phileasfogg3 user
6. [[polkit-bypass]] via PAM environment variables (CVE-2025-6018)
7. [[udisks-abuse]] to mount malicious XFS filesystem (CVE-2025-6019)
8. [[suid-binary]] escalation via crafted SetUID bash binary

## Techniques used

- [[directory-traversal]] — CVE-2025-49132 in Pterodactyl Panel v1.11.10 allows unauthenticated traversal via locale/namespace parameters to include arbitrary .php files
- [[lfi-to-rce]] — Chaining file inclusion with PEAR's pearcmd.php to write webshell using register_argc_argv parameter splitting
- [[hash-cracking]] — Cracking bcrypt hash with hashcat to obtain user password
- [[password-reuse]] — Using cracked database password to access user account via su/SSH
- [[polkit-bypass]] — Abusing PAM .pam_environment file to set XDG_SEAT and XDG_VTNR, bypassing Polkit's allow_active restrictions for SSH sessions
- [[udisks-abuse]] — Exploiting libblockdev XFS resize operation to mount filesystem without security flags, allowing SetUID binary execution
- [[suid-binary]] — Creating SetUID-root bash binary in XFS image mounted during udisks resize operation

## Tools used

- [[nmap]], [[curl]], [[feroxbuster]], [[ffuf]], [[hashcat]], [[john]], [[netcat]]
- olevba, keepassxc-cli, keepass2john, net, smbclient, evil-winrm, dpapi

## Services / ports

- [[http]] (80/443) — Nginx with PHP-FPM, hosting Pterodactyl Panel and Minecraft site
- [[ssh]] (22) — OpenSSH 9.6
- [[ldap]] (389/636/3268/3269) — Active Directory LDAP services
- [[kerberos]] (88) — Windows Kerberos
- [[smb]] (445) — Windows file sharing

## Lessons / notes

- Pterodactyl Panel locale endpoint vulnerability allows including any .php file by using `..` traversal in locale parameter
- The PEAR pearcmd.php technique requires register_argc_argv enabled and uses `+` as argv separator
- For bcrypt cracking, modern John from snap is needed as older versions don't support newer KeePass formats
- openSUSE uses different Polkit rules - SSH sessions normally restricted but can bypass with environment variables
- The XFS udisks exploit requires precise timing during resize operation to execute SUID binary
- CVE-2025-6018 and CVE-2025-6019 chain allows full privilege escalation on openSUSE Leap 15.6
