---
type: machine
title: Pollution
platform: htb
os: linux
difficulty: hard
tags: [ad, linux, web, privesc]
solved: 2026-07-09
sources: [[htb-pollution]]
related: []
---
# Pollution
> Hard Linux box featuring XXE injection for file disclosure, Redis session manipulation for authentication bypass, PHP filter chain for LFI-to-RCE, PHP-FPM abuse for user access, and prototype pollution in a NodeJS API for root privilege escalation.
## Attack path
1. [[xxe]] — Read `/etc/passwd` and Apache configs via blind XXE in XML upload
2. [[redis-session-manipulation]] — Modify Redis session to access developers site with HTTP auth bypass
3. [[php-filter-injection]] — Exploit PHP filter chain for LFI → RCE as www-data
4. [[php-fpm-abuse]] — Abuse FastCGI Process Manager on port 9000 to write SSH key as victor
5. [[prototype-pollution]] — Pollute Object.prototype in NodeJS Express API to spawn SetUID binary and get root
## Techniques used
- [[xxe]] — Blind XXE via external DTD to exfil base64-encoded file contents
- [[htpasswd-cracking]] — Crack Apache MD5 hash to access developers site
- [[redis-session-manipulation]] — Modify PHP session in Redis to set auth=true
- [[php-filter-injection]] — Stack PHP convert filters to generate webshell from LFI
- [[php-fpm-abuse]] — Use cgi-fcgi to inject commands via PHP_VALUE auto_prepend_file
- [[prototype-pollution]] — Exploit lodash merge() to pollute Object.prototype with shell/argv0/NODE_OPTIONS
- [[password-cracking]] — crack SSH key passphrase with john
## Tools used
- [[nmap]] — Port scanning
- [[redis-cli]] — Interact with Redis and modify session data
- [[ffuf]] — Subdomain fuzzing
- [[feroxbuster]] — Directory brute force
- [[hashcat]] — Crack Apache $apr1$ MD5 hash from .htpasswd
- [[john]] — Crack encrypted SSH key passphrase
- [[php-filter-chain-generator]] — Generate PHP filter chain payload
- [[curl]] — HTTP requests and webshell interaction
- [[ssh-keygen]] — Generate SSH key pair
- [[netcat]] — Reverse shell listener
## Services / ports
- [[ssh]] — TCP 22 (OpenSSH 8.4p1)
- [[http]] — TCP 80 (Apache 2.4.54)
- [[redis]] — TCP 6379 (Redis 4.0.9, requires auth)
## Lessons / notes
- XXE file exfil via URL length limits: base64 encoding increases size ~4/3, PHP fails around 3000 chars
- Redis sessions store serialized PHP: `auth|b:1;` for boolean, `auth|s:1:"1";` for string
- PHP filter injection stacks convert.iconv.* and base64-* filters to generate arbitrary PHP code
- PHP-FPM on localhost:9000 accepts FastCGI requests; PHP_VALUE can set auto_prepend_file for code injection
- Node.js prototype pollution via lodash merge() affects child_process.exec() shell/argv0/NODE_OPTIONS properties
- Pollution ran NodeJS API as root, making prototype pollution directly give root access
