---
type: machine
title: Principal
platform: htb
os: linux
difficulty: medium
tags: [java, jwt, web, ssh, certificates, ad]
solved: 2026-07-09
sources: [[htb-principal]]
related: []
---
# Principal
> Java web application using pac4j for JWT authentication, exploited via CVE-2026-29000 to forge encrypted JWTs with only the public key, then password spraying for SSH access and SSH certificate authority abuse for root.

## Attack path
1. Enumerate [[http]] (8080) with [[nmap]] and [[feroxbuster]]
2. Identify pac4j-jwt 6.0.3 vulnerable to CVE-2026-29000
3. Fetch RSA public key from /api/auth/jwks endpoint
4. Forge encrypted JWT with admin role using public key
5. Access dashboard and extract encryptionKey password
6. Password spray against [[ssh]] for svc-deploy user
7. Sign SSH certificate for root principal using CA private key
8. SSH as root using signed certificate

## Techniques used
- [[jwt-forging]] — CVE-2026-29000: forge encrypted JWTs with only public key
- [[password-spray]] — Tried dashboard password against SSH with hydra
- [[ssh-certificate-authentication]] — Used CA key to sign certificate for root principal
- [[ssh-ca-abuse]] — Abused TrustedUserCAKeys configuration to sign user certificates

## Tools used
- [[nmap]]
- [[feroxbuster]]
- [[curl]]
- jwcrypto (Python)
- [[hydra]]
- [[sshpass]]
- [[ssh-keygen]]

## Services / ports
- [[ssh]] (22) — OpenSSH 9.6p1
- [[http]] (8080) — Jetty with pac4j-jwt 6.0.3

## Lessons / notes
- CVE-2026-29000 allows forging JWTs when pac4j processes encrypted tokens without inner signatures
- RSA-OAEP-256 with A256GCM encryption used for JWT envelopes
- Dashboard settings often contain credentials that work for other services
- SSH certificate authorities with TrustedUserCAKeys allow signing certificates for any user
- Without AuthorizedPrincipalsFile, certificate principals map directly to usernames
- PermitsRootLogin prohibit-password still allows certificate-based authentication
- Java/Jetty applications may expose framework versions in HTTP headers
