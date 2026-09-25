---
type: machine
title: Toby
platform: htb
os: linux
difficulty: insane
tags: [linux, web, privesc, container, ad]
solved: 2026-07-09
sources: [[htb-toby]]
related: []
---
# Toby
> Toby is an insane difficulty Linux box involving container escape, database password cracking, and custom PAM module exploitation. The attack path includes exploiting a WordPress backdoor, pivoting through MySQL container, and brute-forcing a custom PAM backdoor.
## Attack path
1. Find and decode obfuscated [[webshell-backdoor]] in WordPress comments
2. Identify XOR-based C2 communication and send reverse shell command
3. Access MySQL database via Docker network and crack Gogs user hash
4. Access personal webapp and generate time-seeded password list
5. Crack MySQL hash and access MySQL container as jack
6. Capture SSH key from automated backup process to access host
7. Analyze custom PAM module and brute-force timing-based password leak
## Techniques used
- [[webshell-backdoor]] — Heavily obfuscated PHP eval chain in WordPress comments
- [[xor-encoding]] — Single-byte XOR communication with variable key
- [[container-escape]] — Lateral movement from WordPress container to MySQL container via Docker network
- [[password-generation]] — Time-seeded random password generation algorithm
- [[ssh-capture]] — Capturing temporary SSH keys from automated backup process
- [[pam-backdoor]] — Custom PAM module with timing-based password character leak
## Tools used
[[nmap]], [[wpscan]], [[pspy]], [[hashcat]], [[chisel]], [[proxychains]], ssh, mysql
## Services / ports
- [[ssh]] (22)
- [[http]] (80) - nginx 1.18.0 with WordPress 5.7.2
## Lessons / notes
- Complex multi-layer obfuscation requires systematic deobfuscation
- XOR encoding with session-based keys provides simple C2 obfuscation
- Docker container networking allows lateral movement between services
- Time-seeded password generation can be brute-forced with known timeframes
- Custom PAM modules may have exploitable side-channel vulnerabilities
