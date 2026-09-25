---
type: source
title: "HTB BigBang writeup"
raw: raw/htb-bigbang.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bigbang]]
---
# Source: HTB BigBang writeup
> Advanced exploitation chain combining WordPress vulnerabilities, glibc buffer overflow, database hash cracking, and Android APK reverse engineering to achieve root access.
## Key facts extracted
- WordPress 6.5.4 with BuddyForms 2.7.7 vulnerable to CVE-2023-26326 and CVE-2024-32830
- glibc iconv buffer overflow (CVE-2024-2961) exploited via PHP filter chains
- WordPress database contains shawking user with password "quantumphysics"  
- Grafana SQLite database contains developer user with password "bigbang"
- Android APK communicates with app.bigbang.htb:9090 using JWT authentication
- Command injection possible via newline characters in output_file parameter
## Filed into
[[bigbang]], [[cve-2023-26326]], [[cve-2024-2961]], [[php-filter-chains]], [[wordpress-db-extraction]], [[grafana-db-cracking]], [[apk-reverse-engineering]], [[command-injection]]
