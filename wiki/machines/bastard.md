---
type: machine
title: "HTB Bastard"
platform: htb
os: windows
difficulty: medium
tags: [windows, web, drupal, rce, kernel-exploit, privesc]
solved: 2026-07-09
sources: [[htb-bastard]]
related: []
---
# HTB Bastard
> Bastard was the 7th box on HTB, presenting a Drupal 7.54 instance with multiple exploitation paths including the Services module RCE, Drupalgeddon2, and Drupalgeddon3 vulnerabilities. The privesc leverages an unpatched Windows Server 2008 R2 vulnerable to MS15-051 kernel exploit.
## Attack path
1. Enumerate [[http]] port 80 to identify Drupal 7.54 via [[nmap]] and droopescan
2. Exploit Drupal Services module RCE via [[drupal-services-rce]] to upload webshell as iusr
3. Privilege escalation from iusr to system via [[ms15-051]] kernel exploit
4. Alternative paths: [[drupalgeddon2]] or [[drupalgeddon3]] with authentication
## Techniques used
- [[drupal-services-rce]] — Unauthenticated RCE in Drupal Services module via /rest endpoint, allowing arbitrary file upload leading to webshell
- [[drupalgeddon2]] — CVE-2018-7600 remote code execution in Drupal < 8.3.9/< 8.4.6/< 8.5.1 via POST to /user/register with malicious form fields
- [[drupalgeddon3]] — CVE-2018-7602 authenticated RCE in Drupal < 7.58/< 8.3.9 requiring valid session and node deletion
- [[ms15-051]] — Windows kernel exploit in win32k.sys for local privilege escalation on unpatched systems
## Tools used
[[nmap]], [[droopescan]], [[searchsploit]], [[hashcat]], [[netcat]]
## Services / ports
- [[http]] (80) - IIS 7.5 hosting Drupal 7.54
- rpc (135, 49154) - Windows RPC services
## Lessons / notes
- Drupal version enumeration via CHANGELOG.txt or droopescan
- Multiple Drupal RCE vulnerabilities exist for different versions
- Unpatched Windows systems require kernel exploits for privesc
- MS15-051 reliable on Windows 7/Server 2008 R2 without hotfixes
