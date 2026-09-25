---
type: machine
title: AirTouch
platform: htb
os: linux
difficulty: medium
tags: [wireless, snmp, wpa2, evil-twin, eap]
solved: 2026-07-09
sources: [[htb-airtouch]]
related: []
---
# AirTouch
> Wireless network penetration testing box featuring SNMP default credentials, WPA2 handshake cracking, and evil twin attacks against WPA2-Enterprise networks.

## Attack path
1. [[snmp-default-credentials]] to get consultant password → [[ssh]] access
2. Capture and [[wpa2-handshake-crack]] on AirTouch-Internet network → Wireless access
3. [[wireshark-decrypt]] WPA2 traffic to recover session cookies → Router admin access
4. [[file-upload-bypass]] with .phtml extension → [[webshell]] on router
5. Recover CA certificates from router → [[evil-twin]] with eaphammer
6. Capture and [[peap-mschapv2-crack]] → Corporate network credentials
7. Use recovered credentials for SSH → [[sudo]] to root

## Techniques used
- [[snmp-default-credentials]] — Default consultant password exposed in SNMP sysDescr
- [[wpa2-handshake-crack]] — Deauth attack to capture WPA2 4-way handshake, crack with aircrack-ng
- [[wireshark-decrypt]] — Use cracked PSK to decrypt wireless traffic and extract HTTP cookies
- [[client-side-role-cookie]] — UserRole cookie enforced client-side, change to "admin" for upload
- [[file-upload-bypass]] — PHP extension filter bypassed using .phtml instead of .php
- [[evil-twin]] — Rogue AP with legitimate certificates to capture PEAP-MSCHAPv2 authentication
- [[peap-mschapv2-crack]] — Captured challenge/response cracked as NetNTLMv1 hash

## Tools used
- [[nmap]], onesixtyone, [[snmpwalk]], [[ssh]], [[aircrack-ng]], [[hashcat]], wireshark, wpa_supplicant, dhclient, [[netcat]], proxychains, eaphammer

## Services / ports
- [[ssh]] (22), [[snmp]] (161/udp), [[http]] (80)

## Lessons / notes
- SNMP often contains sensitive information in system descriptions
- WPA2-PSK handshakes can be captured with deauth attacks and cracked offline
- Evil twin attacks against WPA2-Enterprise require valid certificates to be effective
- PEAP-MSCHAPv2 challenge/response is mathematically equivalent to NetNTLMv1
- Wireless monitoring requires putting interface in monitor mode with airmon-ng
- Client-side cookie validation is a common web vulnerability
- PHP extension filters can often be bypassed with alternative valid extensions
