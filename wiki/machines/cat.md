---
type: machine
title: Cat
platform: htb
os: linux
difficulty: medium
tags: [web, git, xss, sqli, php, sqlite, ad, privesc]
solved: 2026-07-09
sources: [[htb-cat]]
related: []
---
# Cat
> Cat is a Best Cat Competition website where I'll leak the source code from an exposed Git repository, use XSS to capture the admin user's cookie, exploit a SQL injection to get a webshell, crack a hash from the database to pivot users, find another user's password in Apache logs, and exploit a vulnerability in a private Gitea instance to get root.

## Attack path
1. Access exposed [[git-exposure]] to leak source code
2. Use [[xss]] / [[html-injection]] to steal admin cookie (PHPSESSID)
3. Exploit [[sqlite-sqli]] to write [[webshell-upload]]
4. Crack MD5 hash from database for rosa user
5. Find axel password in [[log-poisoning]] from Apache access logs
6. Exploit [[gitea-cve-2024-6886]] stored XSS to read private repo via [[ssrf]]
7. Use leaked admin password for root

## Techniques used
- [[git-exposure]] — Download .git directory with git-dumper to access source code
- [[xss]] — Inject JavaScript in username field to steal admin PHPSESSID cookie
- [[html-injection]] — Bypass input filter with HTML-encoded characters in onerror attribute
- [[sqlite-sqli]] — Stack SQLite queries to write PHP webshell via ATTACH DATABASE
- [[webshell-upload]] — Write PHP webshell to filesystem using SQLite CREATE TABLE
- [[hash-cracking]] — Crack MD5 hashes from SQLite database with CrackStation
- [[log-poisoning]] — Find credentials in Apache access.log from GET requests
- [[gitea-cve-2024-6886]] — Stored XSS in Gitea repository description field
- [[ssrf]] — Use JavaScript fetch() to read internal Gitea repositories

## Tools used
- [[nmap]]
- [[ffuf]]
- git-dumper
- [[curl]]
- sqlmap
- hashcat / CrackStation
- [[ssh]]
- swaks
- evil-winrm

## Services / ports
- [[ssh]] (22)
- [[http]] (80)
- [[smtp]] (25, 587)
- gitea (3000)

## Lessons / notes
- PHPSESSID cookie not HttpOnly, vulnerable to XSS theft
- Input filter blocks `[+*{}',;<>()\\[\\]\\/\\:]` but not `"` or `&`
- HTML-encoded JavaScript executes in onerror attributes without semicolons
- SQLite ATTACH DATABASE allows file writes with .php extension
- Users table contains MD5 hashes (rosa/soyunaprincesarosa)
- axel password in logs: aNdZwgC4tI9gnVXv_e3Q
- Gitea 1.22.0 vulnerable to CVE-2024-6886 stored XSS
- Private repo: administrator/Employee-management with admin credentials
- root password: IKw75eR0MR7CMIxhH0
