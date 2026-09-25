---
type: source
title: "HTB Resource writeup"
raw: raw/htb-resource.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[resource]]
---
# Source: HTB Resource writeup
> In-depth analysis of the Resource HackTheBox machine covering PHAR deserialization, SSH certificate infrastructure, and bash glob vulnerabilities.

## Key facts extracted
- IT ticket system accepts zip attachments and stores uploads
- PHP include() with file_exists check still vulnerable to phar:// filter
- Database contains ticket history with technical details about migration
- HAR file recording during login captured msainristil's credentials
- Old ITRC CA certificate still trusted for SSH authentication
- SSH certificate signing API available on signserv.ssg.htb
- sign_key.sh script has quoteless comparison vulnerability
- Multiple SSH ports indicate containerized or multi-host environment
- Principal validation prevents root_user signing via API

## Filed into
[[resource]], [[phar-deserialization]], [[har-file-extraction]], [[ssh-certificate-signing]], [[bash-glob-leak]]
