---
type: source
title: "HTB BroScience writeup"
raw: raw/htb-broscience.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[broscience]]
---
# Source: HTB BroScience writeup
> Medium Linux box featuring directory traversal for source code analysis, PRNG prediction for activation bypass, PHP deserialization for RCE, password hash cracking, and certificate-based command injection.
## Key facts extracted
- Directory traversal: ..%252f bypasses filter in img.php
- PRNG seeded with time() in generate_activation_code()
- Database credentials: dbuser/RangeOfMotion%777 for broscience database
- Password hash: MD5($salt . $password) with salt "NaCl"
- Bill password: iluvhorsesandgym (from cracked hash)
- Certificate renewal script: /opt/renew_cert.sh with command injection in CN field
- Cron job runs every 2 minutes as root checking certificate expiration
## Filed into
[[broscience]], [[directory-traversal]], [[prng-prediction]], [[php-deserialization]], [[hash-cracking]], [[command-injection]]