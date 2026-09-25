---
type: machine
title: Resource
platform: htb
os: linux
difficulty: hard
tags: [linux, web, privesc, ssh]
solved: 2026-07-09
sources: [[htb-resource]]
related: []
---
# Resource
> A complex IT resource management system involving ticket uploads, SSH certificate authority infrastructure, and API-based signing. The attack path exploits PHAR deserialization, database credential extraction, SSH certificate abuse, and bash globbing vulnerabilities.

## Attack path
1. [[nmap]] identifies two SSH ports suggesting multiple hosts
2. [[phar-deserialization]] via uploaded zip file ticket attachment
3. Database access reveals user credentials and ticket history
4. [[har-file-extraction]] contains msainristil's credentials
5. SSH access to container with old CA signing certificate
6. [[ssh-certificate-signing]] with old CA for root in container
7. Certificate signing API abuse for support user on main host
8. [[bash-glob-leak]] to extract IT CA private key
9. Sign certificate with root_user principal for SYSTEM access

## Techniques used
- [[phar-deserialization]] — PHP phar:// filter to execute code from zip uploads
- [[har-file-extraction]] — HAR files may contain credentials from recorded sessions
- [[ssh-certificate-signing]] — Sign user keys with trusted CA for authentication
- [[bash-glob-leak]] — Wildcard comparison without quotes allows key extraction

## Tools used
[[nmap]] | [[feroxbuster]] | [[mysql]] | [[ssh-keygen]] | [[curl]] | [[netcat]]

## Services / ports
[[http]] (80) | [[ssh]] (22, 2222) | [[mysql]] (internal)

## Lessons / notes
- PHP phar:// filter can execute code from uploaded zip files
- HAR files submitted for troubleshooting may contain active credentials
- SSH certificates provide passwordless authentication when signed by trusted CA
- Multiple CA certificates can be trusted simultaneously on SSH servers
- Bash comparisons without quotes are vulnerable to wildcard expansion
- Certificate signing APIs may not enforce proper principal validation
- AuthorizedPrincipalsFile maps certificate principals to allowed usernames
