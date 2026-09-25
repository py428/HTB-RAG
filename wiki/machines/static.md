---
type: machine
title: Static
platform: htb
os: linux
difficulty: hard
tags: [web, vpn, xdebug, php, format-string, hard, linux, privesc]
solved: 2026-07-09
sources: [[htb-static]]
related: []
---
# Static
> Hard Linux box with multi-stage attack involving corrupted gzip recovery, TOTP bypass, VPN access, Xdebug exploitation, and format string vulnerability. Initial access through recovering TOTP seed from corrupted database backup, pivoting via VPN to internal network, exploiting Xdebug for RCE, then using CVE-2019-11043 against PHP-FPM before privilege escalation via format string exploit in easy-rsa tool.
## Attack path
1. [[gzip-recovery]] — recover TOTP seed from corrupted SQL backup
2. [[ntp-sync]] — synchronize time for TOTP generation
3. [[totp-bypass]] — bypass 2FA using recovered seed
4. [[vpn-pivot]] — connect to internal network via OpenVPN
5. [[xdebug-rce]] — exploit Xdebug remote debugging on PHP server
6. [[cve-2019-11043]] — PHP-FPM fastcgi_split_path_info exploit
7. [[format-string-exploit]] — overwrite easy-rsa path variable via format string

## Techniques used
- [[gzip-recovery]] — extract partial data from corrupted gzip using fixgz
- [[ntp-sync]] — query NTP server for time synchronization
- [[totp-bypass]] — generate valid TOTP tokens using recovered seed
- [[vpn-pivot]] — pivot into internal network using VPN config
- [[xdebug-rce]] — abuse Xdebug remote debugging for code execution
- [[cve-2019-11043]] — exploit PHP-FPM fastcgi path splitting vulnerability
- [[format-string-exploit]] — format string vulnerability in ersatool binary

## Tools used
- [[nmap]] — port scanning and service enumeration
- feroxbuster — directory brute force
- gzip/fixgz — corrupted file recovery
- oathtool/pyotp — TOTP token generation
- ntpdate — NTP time synchronization
- openvpn — VPN client for network pivot
- proxychains — tunneling through VPN
- mysql — database interaction
- CVE-2019-11043 exploit — PHP-FPM exploit
- xdebug client — DBGp client for PHP debugging
- [[nc]] — file transfer and reverse shells
- pwntools — format string exploitation
- pspy — process monitoring

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 7.9p1 Debian
- 2222/tcp — [[ssh]] — OpenSSH 7.6p1 Ubuntu (docker)
- 8080/tcp — [[http]] — Apache 2.4.38
- 123/udp — [[ntp]] — NTP time sync
- 1194/udp — OpenVPN server
- 3306/tcp — MySQL (internal)
- 9000/tcp — Xdebug debugging

## Lessons / notes
- Corrupted gzip files can often be partially recovered with fixgz
- TOTP secrets allow authentication bypass if leaked
- Xdebug with remote debugging enabled provides RCE
- CVE-2019-11043 exploits PHP-FPM path handling for RCE
- Format string vulnerabilities can overwrite global variables
- easy-rsa calls openssl without full path (path hijack opportunity)
- VPN access provides internal network pivot
- Multi-stage attacks require careful enumeration of each component
