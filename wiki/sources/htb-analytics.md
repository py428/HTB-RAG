---
type: source
title: "HTB Analytics writeup"
raw: raw/htb-analytics.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[analytics]]
---
# Source: HTB Analytics writeup

> Complete walkthrough for HTB Analytics box covering Metabase pre-auth RCE exploitation, Docker container escape, and GameOver(lay) kernel privilege escalation.

## Key facts extracted

- **Vulnerable service**: Metabase analytics platform exposed on data.analytical.htb
- **Initial access**: CVE-2023-38646 — pre-auth RCE via setup token leak and H2 trigger injection
- **Container escape**: Credentials found in environment variables (META_USER/META_PASS)
- **Privilege escalation**: GameOver(lay) kernel exploit targeting OverlayFS in Ubuntu 22.04
- **Attack surface**: Two websites (main site and data subdomain) sharing JWT authentication

## Filed into

[[analytics]], [[metabase-cve-2023-38646]], [[container-escape-gameoverlay]], [[docker-enumeration]]
