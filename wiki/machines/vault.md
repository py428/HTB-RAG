---
type: machine
title: Vault
platform: htb
os: linux
difficulty: medium
tags: [web, php, upload-bypass, openvpn, port-forwarding, gpg, vm-escape]
solved: 2026-07-09
sources: [[htb-vault]]
related: []
---
# Vault
> Multi-VM environment requiring chaining through DNS and firewall to reach the vault. Exploitation involves PHP upload filter bypass, OpenVPN config RCE, SSH credential harvesting, and GPG-encrypted flag extraction.

## Attack path
1. [[php-extension-bypass]] — Upload PHP5 webshell via `changelogo.php` extension filter bypass
2. [[openvpn-rce]] — Craft malicious OpenVPN config with `up` command for reverse shell
3. [[ssh-pivot]] — Use harvested credentials to pivot through network
4. [[firewall-bypass]] — Add secondary IP or use allowed source ports (53, 4444) to reach vault
5. [[gpg-decrypt]] — Extract encrypted flag from vault and decrypt on main host with known key

## Techniques used
- [[php-extension-bypass]] — Extension whitelist bypassed with `.php5` extension
- [[openvpn-rce]] — OpenVPN config `up` directive allows command execution on connection
- [[firewall-bypass]] — Direct access by adding IP to interface or using allowed source ports
- [[gpg-decrypt]] — GPG-encrypted flag requires key on different host
- [[vm-escape]] — SPICE protocol allows VM console access for recovery mode

## Tools used
- [[nmap]]
- [[gobuster]]
- [[curl]]
- [[netcat]]
- [[ssh]]
- [[remmina]] (SPICE client)
- [[base32]]

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 7.2p2 Ubuntu
- 80/tcp — [[http]] — Apache httpd 2.4.18 (Ubuntu)
- 4444/tcp — [[ssh]] — Custom SSH port on firewall

## Lessons / notes
- Multi-VM setup: ubuntu host, DNS VM (192.168.122.4), firewall VM (192.168.122.5), vault VM (192.168.5.2)
- PHP5 extension accepted by upload filter
- OpenVPN config `up` command runs as root on connection
- Firewall allows traffic from source ports 53 and 4444
- SPICE ports accessible via `ps` output (5900-5902)
- GPG key: `itscominghome` (from `/home/dave/Desktop/key` on ubuntu)
