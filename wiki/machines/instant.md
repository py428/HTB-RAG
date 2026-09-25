---
type: machine
title: Instant
platform: htb
os: linux
difficulty: medium
tags: [android, web, jwt, file-read, privesc]
solved: 2026-07-09
sources: [[htb-instant]]
related: []
---
# Instant
> Instant is a Linux medium box starting with Android application reverse engineering to find a hardcoded JWT token and subdomains. The token provides admin access to an API with a file read vulnerability. Root access requires decrypting a SolarPuTTY sessions backup file using credentials obtained from password cracking.

## Attack path
1. Reverse engineer Android APK to find hardcoded JWT token and additional subdomains
2. Use admin JWT token to access Swagger UI and discover admin API endpoints
3. Exploit [[file-read]] via `/api/v1/admin/read/log` with directory traversal
4. Read SSH private key from user home directory
5. Find SolarPuTTY backup file in `/opt/backups/`
6. Crack user password from SQLite database using hashcat with Werkzeug hash format
7. Decrypt SolarPuTTY sessions to obtain root password

## Techniques used
- [[apk-reversing]] — String analysis and code review using jadx-gui
- [[jwt-hardcoded]] — Hardcoded admin JWT token in Android application
- [[directory-traversal]] — Path traversal in admin log read endpoint
- [[sqlite-extraction]] — Database extraction and password hash cracking
- [[solarputty-decrypt]] — SolarPuTTY session file decryption for credential extraction

## Tools used
- [[nmap]], [[feroxbuster]], [[jadx]], [[jwt.io]], [[curl]], [[hashcat]], [[solarputtydecrypt]], [[solarputtycracker]], [[python]]

## Services / ports
- 22/tcp — [[ssh]]
- 80/tcp — [[http]] (Apache with reverse proxy to Flask APIs)
- 8888/tcp — Flask API (mywalletv1.instant.htb)
- 8808/tcp — Swagger UI (swagger-ui.instant.htb)

## Lessons / notes
- Android APK reverse engineering often reveals hardcoded API tokens and endpoints
- JWT tokens can have extremely long expiration dates (years)
- Werkzeug password hashes can be converted for hashcat cracking
- SolarPuTTY stores credentials in encrypted session files that can be cracked
- Maven settings.xml files may contain repository credentials
