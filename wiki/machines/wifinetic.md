---
type: machine
title: Wifinetic
platform: htb
os: linux
difficulty: easy
tags: [linux, wifi, ftp, wps, wireless, password-reuse]
solved: 2026-07-09
sources: [[htb-wifinetic]]
related: []
---
# Wifinetic
> Wifinetic is an easy Linux box focusing on wireless network exploitation. Initial access is achieved through anonymous FTP access containing OpenWRT configuration files with a WPA pre-shared key that also works for SSH. Privilege escalation involves using the reaver tool to perform a WPS pixie dust attack on a virtualized wireless interface, recovering the root password which matches the WPA PSK.

## Attack path
1. [[anonymous-ftp]] access → download OpenWRT backup configuration
2. [[config-file-analysis]] of OpenWRT wireless config → extract WPA PSK
3. [[password-reuse]] → SSH as netadmin using WPA PSK
4. [[wps-pixie-dust]] attack via reaver → recover root password matching WPA PSK

## Techniques used
- [[anonymous-ftp]] — vsftpd 3.0.3 configured with anonymous login and backup files
- [[config-file-analysis]] — OpenWRT wireless configuration contains WPA PSK in plaintext
- [[password-reuse]] — WPA pre-shared key also used for netadmin SSH authentication
- [[wps-pixie-dust]] — Reaver tool exploits WPS vulnerability to recover WPA PSK, which matches root password

## Tools used
- [[nmap]], [[ftp]], [[curl]], [[crackmapexec]], [[ssh]], [[reaver]], [[hydra]]

## Services / ports
- 21/tcp — [[ftp]] (vsftpd 3.0.3) anonymous access
- 22/tcp — [[ssh]] (OpenSSH 8.2)
- 53/udp — [[dns]]

## Lessons / notes
- FTP anonymous access can provide valuable configuration files
- OpenWRT wireless configurations often contain credentials in plaintext
- WPA pre-shared keys are frequently reused across different services
- WPS pixie dust attacks can recover WPA passwords in seconds on vulnerable routers
- Reaver requires CAP_NET_RAW capability to interact with wireless interfaces
- Virtual wireless interfaces can be used for testing wireless attacks on HTB
- Password reuse between wireless and SSH credentials is common in real environments
