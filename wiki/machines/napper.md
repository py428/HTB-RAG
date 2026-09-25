---
type: machine
title: Napper
platform: htb
os: windows
difficulty: hard
tags: [windows, malware, privesc, custom-laps]
solved: 2026-07-09
sources: [[htb-napper]]
related: []
---
# Napper
> Hard-difficulty Windows box featuring IIS backdoor exploitation, .NET reverse shell development, custom LAPS password extraction from Elastic database, and UAC bypass for administrator access.

## Attack path
1. Find credentials in blog post for [[http]] basic auth
2. Access internal blog post about IIS malware Naplistener
3. Build custom .NET DLL reverse shell for backdoor exploitation  
4. Gain initial foothold as ruben via backdoor on TCP 4386
5. Find custom LAPS implementation in Elastic database
6. Write Go program to extract seed and decrypt password blob
7. Use [[runascs]] with [[uac-bypass]] to gain administrator access

## Techniques used
- [[iis-backdoor]] — Custom IIS malware processing base64-encoded .NET assemblies via POST parameter
- [[dotnet-reverse-shell]] — Build C# DLL with TCP reverse shell as Run class constructor
- [[elastic-database]] — Query Elastic DB for seed and encrypted password blob
- [[custom-laps]] — Extract and decrypt password from custom LAPS implementation
- [[uac-bypass]] — Use RunasCs.exe with --bypass-uac flag for elevated privileges

## Tools used
[[nmap]], [[ffuf]], [[mcs]], [[base64]], [[nc]], [[chisel]], [[curl]], [[RunasCs]]

## Services / ports
[[http]] (80/443), [[smb]] (445)

## Lessons / notes
- IIS backdoor listens on TCP 4386 with path `/ews/MsExgHealthCheckd/` expecting POST parameter `sdafwe3rwe23`
- Backdoor loads base64-encoded assembly and invokes Run class constructor
- Custom LAPS implementation stores encrypted passwords in Elastic database
- Password encryption uses AES-CFB with key derived from random seed
- Seed changes every 5 minutes requiring real-time extraction and decryption
- RunasCs.exe can bypass UAC to get full administrator token
- Backup user in Administrators group but UAC blocks direct access to Desktop folder
- Checkmk agent automation maintains password rotation and system cleanup