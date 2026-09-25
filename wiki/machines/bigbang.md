---
type: machine
title: "HTB BigBang"
platform: htb
os: linux
difficulty: hard
tags: [linux, wordpress, cve-2024-2961, apk-reverse, command-injection, privesc]
solved: 2026-07-09
sources: [[htb-bigbang]]
related: []
---
# HTB BigBang
> BigBang was a hard Linux box featuring WordPress with BuddyForms plugin. Exploitation required chaining CVE-2023-26326 for file upload with CVE-2024-2961 for glibc buffer overflow RCE. Post-exploitation involved WordPress database password reuse, Grafana database hash cracking, and Android APK reverse engineering leading to command injection.
## Attack path
1. Enumerate [[wordpress]] site with WPScan to identify BuddyForms 2.7.7 with [[cve-2023-26326]]
2. Exploit BuddyForms SSRF to upload GIF files and read local files via PHP filter chains  
3. Chain with [[cve-2024-2961]] glibc iconv buffer overflow for RCE as www-data
4. Extract WordPress database credentials from wp-config.php and crack shawking user hash
5. Pivot via SSH to shawking, then access Grafana database to crack developer password
6. Reverse engineer satellite APK to find API endpoints and command injection for root shell
## Techniques used
- [[cve-2023-26326]] — BuddyForms unauthenticated PHAR deserialization and SSRF for arbitrary file upload
- [[php-filter-chains]] — Complex PHP filter chains using wrapwrap for arbitrary file read with GIF prefix bypass
- [[cve-2024-2961]] — glibc iconv buffer overflow exploitation requiring /proc/self/maps read via PHP filters
- [[wordpress-db-extraction]] — Extract WordPress user hashes from database for password cracking
- [[grafana-db-cracking]] — Extract and crack Grafana PBKDF2-HMAC-SHA256 hashes from SQLite database
- [[apk-reverse-engineering]] — Decompile Android APK with JADX to identify API endpoints and authentication
- [[command-injection]] — Newline injection in output_file parameter for command execution via subprocess
## Tools used
[[nmap]], [[wpscan]], [[wrapwrap]], [[hashcat]], [[jadx]], [[ffuf]], [[curl]], [[john]]
## Services / ports
- [[http]] (80) - Apache 2.4.62 hosting WordPress 6.5.4
- [[ssh]] (22) - OpenSSH 8.9p1
- grafana (3000) - Grafana monitoring interface
- satellite-api (9090) - Python Flask satellite control API
## Lessons / notes
- Complex exploit chaining may require bypassing modern PHP protections
- WordPress plugin vulnerabilities can provide SSRF and file read primitives
- glibc vulnerabilities in iconv can be exploited via PHP filter chains
- Mobile applications often contain hardcoded API endpoints and logic
- Command injection via newline characters can bypass shell metacharacter filtering
