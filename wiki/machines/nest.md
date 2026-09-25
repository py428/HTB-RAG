---
type: machine
title: Nest
platform: htb
os: windows
difficulty: easy
tags: [windows, smb, re, privesc]
solved: 2026-07-09
sources: [[htb-nest]]
related: []
---
# Nest
> Easy-difficulty Windows box focused on SMB enumeration, .NET reverse engineering, and custom service exploitation with multiple privilege escalation paths.

## Attack path
1. Access [[smb]] share anonymously and find password for TempUser
2. Use Notepad++ config file to discover hidden directory path
3. Find Visual Basic project with password decryption code
4. Reverse engineer .NET decryption to obtain C.Smith credentials  
5. Access custom HQK Reporting service to get encrypted admin password
6. Debug HqkLdap.exe binary to extract administrator credentials
7. Gain SYSTEM via [[psexec]] or alternative paths

## Techniques used
- [[smb-enumeration]] — Anonymous SMB access and share traversal
- [[dotnet-reversing]] — Analyze and debug .NET binaries to extract credentials
- [[custom-service]] — Exploit HQK Reporting Service on TCP 4386 with debug password
- [[binary-debugging]] — Use dnSpy to debug .NET executable and extract decrypted password from memory
- [[ads-alternate-data-stream]] — Password stored in NTFS alternate data stream

## Tools used
[[nmap]], [[smbclient]], [[smbmap]], [[dnSpy]], [[telnet]], [[psexec]]

## Services / ports
[[smb]] (445), custom HQK Reporting Service (4386)

## Lessons / notes
- SMB anonymous access can reveal credentials in HR documents
- Notepad++ config file history shows recently accessed files including hidden paths
- .NET Visual Basic project includes encryption/decryption functions using AES with static key
- HQK Reporting Service requires debug password to unlock additional commands
- Administrator password stored encrypted in LDAP configuration file
- .NET binaries can be debugged to view decrypted values in memory during execution
- NTFS alternate data streams can hide files that don't appear in directory listings
- Multiple unintended paths existed including PSExec as initial user and various service exploits