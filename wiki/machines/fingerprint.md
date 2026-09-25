---
type: machine
title: Fingerprint
platform: htb
os: linux
difficulty: insane
tags: [linux, web, java, crypto]
solved: 2026-07-09
sources: [[htb-fingerprint]]
related: []
---
# Fingerprint
> An insanely complex multi-stage box requiring execute-after-redirect vulnerability, HQL injection, XSS for fingerprint theft, Java deserialization, ECB padding oracle attack, SSH key brute forcing with SUID binary, and finally AES cookie manipulation for admin access.
## Attack path
1. Exploit execute-after-redirect on /admin to view Flask source via [[directory-traversal]]
2. Extract database credentials and SECRET key from source code
3. Brute force HQL injection to extract admin credentials and fingerprint
4. Use XSS to steal admin browser fingerprint and gain login
5. Craft custom Java deserialization payload with Maven and ysoserial
6. Upload malicious serialized objects and exploit command injection in UserProfileStorage
7. Use [[suid-binary]] cmatch to brute force SSH private key character-by-character
8. Crack encrypted SSH key using database password
9. Perform ECB padding oracle attack to leak SECRET from beta Flask application
10. Craft admin cookie and use directory traversal to read root flag
## Techniques used
- [[execute-after-redirect]] — View sensitive data by intercepting 302 responses
- [[hqli]] — Hibernate Query Language injection for database enumeration
- [[xss]] — Cross-site scripting to steal admin fingerprint for authentication
- [[java-deserialization]] — Custom Java payload exploiting command injection in deserialization
- [[ssh-key-brute-force]] — Character-by-character brute forcing using SUID cmatch binary
- [[ecb-padding-oracle]] — Byte-by-byte ECB encryption analysis to leak secret key
- [[cookie-manipulation]] — Craft admin cookies using leaked SECRET for privilege escalation
## Tools used
- [[nmap]], [[feroxbuster]], [[maven]], [[ysoserial]], [[python]]
- [[curl]], [[netcat]], [[ssh]], [[john]], [[openssl]]
## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 7.6p1 Ubuntu
- 80/tcp — [[http]] — Werkzeug/Flask application
- 8080/tcp — [[http]] — GlassFish Server with Java application
- 8088/tcp — [[http]] — Beta Flask application (localhost only)
## Lessons / notes
- Execute-after-redirect vulnerabilities can expose sensitive data in response bodies
- HQL injection requires different syntax than SQL but follows similar principles
- XSS can be used to steal client-side fingerprints for authentication bypass
- Java deserialization payloads can be crafted with Maven for specific application exploitation
- ECB mode encryption is vulnerable to padding oracle attacks that can leak plaintext
- SUID binaries can be abused for brute forcing file contents character-by-character
