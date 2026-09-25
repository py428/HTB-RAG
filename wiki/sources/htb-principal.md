---
type: source
title: "HTB Principal writeup"
raw: raw/htb-principal.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[principal]]
---
# Source: HTB Principal writeup
> Detailed analysis of Principal, a Medium Java box featuring CVE-2026-29000 JWT authentication bypass, password reuse, and SSH certificate authority abuse.

## Key facts extracted
- Jetty webserver with pac4j-jwt 6.0.3 on Ubuntu 24.04
- CVE-2026-29000: authentication bypass in JwtAuthenticator for encrypted JWTs
- RSA public key available at /api/auth/jwks (kid: enc-key-1)
- JWT encryption: RSA-OAEP-256 + A128GCM (actually A256GCM)
- Dashboard password: D3pl0y_$$H_Now42! for svc-deploy SSH
- SSH CA keys at /opt/principal/ssh/ with deployers group access
- TrustedUserCAKeys configured in sshd_config.d/60-principal.conf
- No AuthorizedPrincipalsFile, so principals map to usernames directly

## Filed into
[[principal]], [[jwt-forging]], [[password-spray]], [[ssh-certificate-authentication]], [[ssh-ca-abuse]]
