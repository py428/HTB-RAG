---
type: source
title: "HTB Bolt writeup"
raw: raw/htb-bolt.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bolt]]
---
# Source: HTB Bolt writeup
> Comprehensive writeup covering Docker image analysis, SSTI exploitation, and Passbolt abuse chain.

## Key facts extracted
- Docker image available for download from bolt.htb/download
- Database contained admin hash (md5crypt) that cracked to "deadbolt"
- Demo site invite code: XNSS-HSJW-3NGU-8XTJ found in source code
- SSTI vulnerability in /confirm/changes/<token> via render_template_string
- Passbolt database credentials: passbolt / rT2;jW7<eY8!dX8}pQ8%
- Eddie's Passbolt key password: merrychristmas

## Filed into
[[bolt]], [[docker-image-analysis]], [[ssti]], [[passbolt-abuse]]
