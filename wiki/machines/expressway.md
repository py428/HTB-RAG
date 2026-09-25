---
type: machine
title: Expressway
platform: htb
os: linux
difficulty: easy
tags: [linux, vpn, ike, sudo, cve]
solved: 2026-07-09
sources: [[htb-expressway]]
related: []
---
# Expressway
> Linux VPN server with IKE aggressive mode PSK leak, sudo CVE exploitation for root.

## Attack path
1. [[ike-psk-crack]] — Aggressive mode leaks PSK via [[ike-scan]] 
2. SSH access with cracked PSK credentials
3. [[cve-2025-32462]] or [[cve-2025-32463]] in sudo for root privilege escalation

## Techniques used
- [[ike-psk-crack]] — IKE aggressive mode pre-shared key extraction and cracking
- [[cve-2025-32462]] — Sudo hostname spoofing vulnerability
- [[cve-2025-32463]] — Sudo chroot nsswitch.conf arbitrary code execution

## Tools used
- [[nmap]], [[ike-scan]], [[hashcat]], [[netexec]], [[john]]

## Services / ports
- [[ssh]] (22), [[isakmp]] (500), [[tftp]] (69)

## Lessons / notes
- IKE aggressive mode is inherently insecure as it leaks identity before authentication
- Multiple sudo CVEs available; CVE-2025-32463 (chroot) easier than CVE-2025-32462 (hostname spoof)
- TFTP often overlooked but can host configuration files
- sudo versions matter — different vulnerabilities across 1.9.13p3 vs 1.9.17