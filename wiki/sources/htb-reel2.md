---
type: source
title: "HTB Reel2 writeup"
raw: raw/htb-reel2.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[reel2]]
---
# Source: HTB Reel2 writeup
> Realistic Windows attack simulation covering username enumeration from social media, OWA password spraying, NTLM hash capture via phishing, JEA escape techniques, and custom JEA function abuse for privilege escalation.

## Key facts extracted
- Wallstant social media site on port 8080 with user profiles and posts
- OWA accessible on port 443 with GAL enumeration exposing all users
- SprayingToolkit used to generate usernames and spray OWA with Summer2020 password
- Responder captured NTLMv2 hash when recipient clicked phishing link
- JEA limited shell escape via script blocks and function definitions
- StickyNotes stored jea_test_account credentials in LevelDB format
- Custom Check-File function in JEA configuration allowed reading arbitrary files via path traversal

## Filed into
[[reel2]], [[password-spray]], [[ntlm-relay]], [[jea-escape]], [[sticky-notes-creds]], [[jea-abuse]]
