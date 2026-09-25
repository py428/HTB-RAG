---
type: machine
title: "HTB BigHead"
platform: htb
os: windows
difficulty: insane
tags: [windows, buffer-overflow, php-include, tunneling, keepass-cracking, privesc]
solved: 2026-07-09
sources: [[htb-bighead]]
related: []
---
# HTB BigHead
> BigHead was an insane Windows box requiring custom buffer overflow exploitation against BigheadWebSrv, SSH tunneling with Bitvise, PHP LFI bypass, and KeePass database cracking with keyfile extraction from Alternate Data Streams.
## Attack path
1. Enumerate subdomains to find dev.bighead.htb with custom BigheadWebSrv 1.0  
2. Analyze GitHub repo for vulnerable BigheadWebSrv and develop buffer overflow exploit
3. Exploit buffer overflow to get shell as nelson, then find SSH credentials in registry
4. Create [[ssh-tunneling]] using chisel to reach internal SSH on port 2020
5. Access nginx account via SSH, escape BvShell jail via [[php-include]] in testlink
6. Find KeePass database in ADS and crack with keyfile to obtain root flag
## Techniques used
- [[buffer-overflow]] — Custom stack buffer overflow in BigheadWebSvr URL handler with egghunter shellcode
- [[ssh-tunneling]] — Reverse port forwarding with chisel to access internal SSH server  
- [[php-include]] — Local file inclusion bypass in testlink linkto.php via PiperCoinID parameter
- [[ads-extraction]] — Extract KeePass database from Alternate Data Stream using bash
- [[keepass-cracking]] — Crack KeePass database with keyfile using keepass2john and hashcat
## Tools used
[[nmap]], [[gobuster]], [[wfuzz]], [[john]], [[hashcat]], [[kpcli]], [[chisel]], [[bash]]
## Services / ports
- [[http]] (80) - nginx 1.14.0 and custom BigheadWebSvr 1.0 on dev.bighead.htb
- [[ssh]] (2020) - Bitvise SSH server internally accessible
- [[http]] (5080) - TestLink PHP application accessible via tunnel
## Lessons / notes
- Custom web server vulnerabilities require manual analysis and exploit development
- Internal services may require SSH tunneling for access
- Windows Alternate Data Streams can hide important files like KeePass databases  
- KeePass databases may require both password and keyfile for access
- PHP application vulnerabilities can provide file inclusion primitives even in restricted environments
