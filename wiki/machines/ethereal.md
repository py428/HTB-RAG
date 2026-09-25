---
type: machine
title: Ethereal
platform: htb
os: windows
difficulty: insane
tags: [windows, web, command-injection, code-signing]
solved: 2026-07-09
sources: [[htb-ethereal]]
related: []
---
# Ethereal
> Challenging Windows box featuring FTP anonymous access with encrypted password vault, HTTP basic auth bruteforcing, blind command injection with DNS exfiltration, LNK file poisoning for user escalation, and code signing with CA certificates for Administrator access.

## Attack path
1. Anonymous FTP access → extract PasswordBox database → recover credentials
2. [[hydra]] bruteforce HTTP basic auth on TCP 8080
3. [[command-injection]] in ping panel with [[dns-exfiltration]] for initial shell
4. [[lnk-poisoning]] via Visual Studio shortcut to escalate to jorge
5. [[code-signing]] abuse with CA certificates to obtain Administrator shell

## Techniques used
- [[password-vault-recovery]] — Extracting and decrypting PasswordBox encrypted database from FTP disk images
- [[hydra]] — Bruteforcing HTTP basic auth using credentials from password vault
- [[command-injection]] — Injecting commands via ping panel using Windows conditional execution operators
- [[dns-exfiltration]] — Using nslookup for data exfiltration when direct network access is blocked
- [[lnk-poisoning]] — Replacing shortcut file to execute malicious payload when higher-privilege user clicks
- [[code-signing]] — Creating code signing certificate from CA and signing MSI for automatic execution

## Tools used
- [[nmap]], [[hydra]], [[openssl]], [[wfuzz]], pbox, lnkup, signtool, EMCO MSI Package Builder

## Services / ports
- [[ftp]] (21), [[http]] (80/8080)

## Lessons / notes
- FTP anonymous access may contain disk images with valuable data
- PasswordBox password manager uses AES encryption; password can be guessed or brute-forced
- DNS exfiltration useful when other network protocols are blocked by firewall
- OpenSSL can be used for encrypted reverse shells when PowerShell is unavailable
- LNK files can be poisoned to execute arbitrary commands when clicked by other users
- Code signing certificates from CA can sign binaries that will execute automatically
- Firewall rules can be enumerated via netsh or by testing outbound connections
