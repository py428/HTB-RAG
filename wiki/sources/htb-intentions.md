---
type: source
title: "HTB Intentions writeup"
raw: raw/htb-intentions.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[intentions]]
---
# Source: HTB Intentions writeup
> Comprehensive walkthrough covering second-order SQL injection, ImageMagick exploitation, Git credential harvesting, and creative file reading via capability abuse.

## Key facts extracted
- Laravel application with v2 API using client-side bcrypt hashing
- ImageMagick processes images with arbitrary MSL file upload capability
- Git repository contains hardcoded test credentials in commit history
- DMCA scanner has CAP_DAC_READ_SEARCH capability for file reading

## Filed into
[[intentions]], [[second-order-sqli]], [[client-side-hashing]], [[imagemagick-arbitrary-object]], [[git-credential-harvesting]], [[capability-abuse]], [[hash-brute-force]]
