---
type: technique
title: AS-REP Roasting
tags: [ad, windows, kerberos, authentication, credential-access]
platforms: [windows]
mitre: [T1558.004]
updated: 2026-07-09
---

# AS-REP Roasting

## What it is
For domain accounts that have **"Do not require Kerberos preauthentication"** (`UF_DONT_REQUIRE_PREAUTH`) set, the KDC will hand back an AS-REP (authentication reply) to *anyone* who asks for that user — no password needed. That AS-REP contains material encrypted with a key derived from the user's password, which can be cracked offline like a hash.

## When it works
- You have a list of **valid usernames** (this is the real prerequisite — see [[kerberos-username-enumeration]]).
- At least one of them has preauth disabled. Common for service accounts or misconfigured users.
- Requires **no credentials** of your own — it's a pre-auth attack.

## How it's done
Request the AS-REPs, then crack:
```
# Grab AS-REP hashes for a known user list (Impacket)
GetNPUsers.py -dc-ip dc.absolute.htb -usersfile valid_users absolute.htb/

# Crack (hashcat mode 18200 = Kerberos 5 AS-REP etype 23)
hashcat asrep.hash /usr/share/wordlists/rockyou.txt -m 18200
```
Tools: [[impacket]] `GetNPUsers.py`, [[hashcat]], or Rubeus `asreproast` from Windows.

## Observed on
- [[absolute]] — `d.klay` had preauth disabled; hash cracked to `Darkmoonsky248girl`. Username list came from exiftool image metadata.
- [[forest]] — `svc-alfresco` had preauth disabled; cracked to `s3rvice` (user list from RPC null session).

## Variants & pitfalls
- **NTLM may be disabled** even after you get the plaintext password (Protected Users). The cracked password still authenticates — but only over **Kerberos** (`-k`). See [[ntlm-disabled-protected-users]].
- Returns only `etype 23` (RC4) hashes when preauth is off, which are fast to crack.

## See also
[[kerberos-username-enumeration]], [[ntlm-disabled-protected-users]], [[impacket]], [[hashcat]]
