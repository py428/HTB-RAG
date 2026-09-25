---
type: machine
title: WifineticTwo
platform: htb
os: linux
difficulty: medium
tags: [linux, wifi, openplc, wps, openwrt, ci-cd]
solved: 2026-07-09
sources: [[htb-wifinetictwo]]
related: []
---
# WifineticTwo is a medium Linux box featuring OpenPLC industrial control software and wireless network exploitation. Initial access exploits CVE-2021-31630, a command injection vulnerability in OpenPLC's hardware layer code execution. The box contains a wireless interface that can scan for and attack WPS-enabled access points using pixie dust attacks. After connecting to the wireless network, OpenWRT is discovered with no root password set, providing multiple paths to root access including SSH key upload, cron job execution, and SSH with empty password.

## Attack path
1. [[cve-2021-31630]] (OpenPLC RCE) → shell as root on attica01 container
2. [[wireless-scanning]] via iw → discover plcrouter AP with WPS enabled
3. [[wps-pixie-dust]] attack via OneShot → recover WPA PSK
4. [[wifi-connection]] using recovered credentials → access wireless network
5. [[port-forwarding]] via chisel → access OpenWRT on 192.168.1.1
6. [[default-credentials]] (empty root password) → root on OpenWRT via SSH/cron/SSH keys

## Techniques used
- [[cve-2021-31630]] — OpenPLC v3 hardware layer accepts arbitrary C code execution
- [[wireless-scanning]] — Used iw dev wlan0 scan to identify nearby access points and WPS status
- [[wps-pixie-dust]] — OneShot tool exploits WPS vulnerability to recover WPA PSK in seconds
- [[wifi-connection]] — Connected to plcrouter network using wpa_supplicant and dhclient
- [[port-forwarding]] — Created chisel tunnel to access OpenWRT web interface from attacking machine
- [[default-credentials]] — OpenWRT root account has no password by default, allowing SSH access
- [[cron-job-abuse]] — OpenWRT web interface allows arbitrary cron job creation for reverse shells
- [[ssh-key-abuse]] — OpenWRT web interface permits SSH key upload for authentication

## Tools used
- [[nmap]], [[curl]], [[msfvenom]], [[chisel]], [[python]], [[ssh]], [[netcat]]

## Services / ports
- 22/tcp — [[ssh]] (OpenSSH 8.2)
- 80/tcp — [[http]] (OpenPLC)
- 8080/tcp — [[http]] (OpenPLC web interface)
- 192.168.1.1:22/tcp — [[ssh]] (OpenWRT)
- 192.168.1.1:80/tcp — [[http]] (OpenWRT LuCI)
- 192.168.1.1:443/tcp — [[https]] (OpenWRT LuCI)

## Lessons / notes
- OpenPLC default credentials (openplc:openplc) are often unchanged in production environments
- Industrial control systems may have web interfaces with command injection vulnerabilities
- WPS pixie dust attacks are significantly faster than brute force WPS cracking
- Virtual wireless interfaces allow testing wireless attacks in cloud environments
- OpenWRT default configuration often has no root password set
- Multiple privilege escalation paths may exist on embedded systems (cron/SSH/keys)
- Port forwarding tools like chisel are essential when attacking networks behind wireless barriers
- CI/CD build systems often run with excessive privileges making them valuable targets
