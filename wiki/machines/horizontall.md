---
type: machine
title: Horizontall
platform: htb
os: linux
difficulty: easy
tags: [linux, web, strapi, laravel]
solved: 2026-07-09
sources: [[htb-horizontall]]
related: []
---
# Horizontall
> Easy Linux box featuring Strapi CMS with two CVE exploits for initial access (password reset and RCE), followed by Laravel application on localhost with debug mode enabled leading to deserialization attack for root.
## Attack path
1. Enumerate [[http]] (80) redirecting to horizontall.htb and api-prod.horizontall.htb
2. Identify Strapi 3.0.0-beta.17.4 on port 1337 via /admin/strapiVersion
3. Exploit CVE-2019-18818 to reset admin password (empty code bypass)
4. Authenticate to Strapi admin panel
5. Exploit CVE-2019-19609 command injection in plugin installation for shell as strapi
6. Find Laravel application on localhost:8000 via SSH tunnel
7. Trigger Laravel debug crash at /profiles to leak configuration
8. Exploit Laravel debug mode with phar deserialization for root shell
## Techniques used
- [[strapi-password-reset]] — CVE-2019-18818 bypass password reset with empty code object
- [[strapi-auth-rce]] — CVE-2019-19609 command injection in plugin install endpoint
- [[deserialization]] — Laravel debug mode PHAR deserialization to monolog/rce1
- [[laravel-debug-rce]] — Exploit debug information leak for remote code execution
## Tools used
- [[nmap]]
- [[feroxbuster]]
- [[gobuster]]
- [[curl]]
- python (CVE exploit scripts)
- phpggc (PHAR payload generator)
## Services / ports
- [[http]] (80) — nginx 1.14.0 redirecting to horizontall.htb
- [[ssh]] (22) — OpenSSH 7.6p1 Ubuntu
- [[http]] (1337) — Strapi CMS (localhost only)
- [[http]] (8000) — Laravel PHP framework (localhost only)
## Lessons / notes
- Strapi 3.0.0-beta versions vulnerable to password reset and RCE
- CVE-2019-18818 sends empty code object {} to bypass reset token verification
- CVE-2019-19609 injects commands via plugin parameter in install/uninstall endpoints
- Laravel debug mode exposes stack traces and configuration
- PHAR deserialization can achieve RCE via Monolog handler chain
- SSH tunneling useful to access localhost-only services
