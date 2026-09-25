---
type: source
title: "HTB Talkative writeup"
raw: raw/htb-talkative.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[talkative]]
---
# Source: HTB Talkative writeup
> Hard Linux box featuring multi-container communications platform. Long exploit chain: Jamovi R code execution → Bolt credential extraction → Twig template injection → container hopping → MongoDB privilege escalation → Rocket Chat webhook abuse → Docker container escape via CAP_DAC_READ_SEARCH.

## Key facts extracted
- Jamovi Rj editor allows system() calls for RCE (Ctrl+Shift+Enter to run)
- Bolt credentials found in bolt-administration.omv: admin / jeO09ufhWD<s
- Twig SSTI payload: {{_self.env.display("id")}} works in index.twig
- MongoDB on 172.17.0.2 contains Rocket Chat users in meteor database
- Container has CAP_DAC_READ_SEARCH capability for file read/write
- Shocker exploit uses open() + ioctl() to access host filesystem
- Alternative root via /etc/passwd overwrite using Shocker write capability

## Filed into
[[talkative]], [[r-code-execution]], [[zip-archive-extraction]], [[template-injection]], [[mongodb-privilege-escalation]], [[javascript-reverse-shell]], [[docker-capability-abuse]]