---
type: source
title: "HTB BountyHunter writeup"
raw: raw/htb-bountyhunter.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bountyhunter]]
---
# Source: HTB BountyHunter writeup
> XXE exploitation walkthrough from POC to shell via PHP filter wrappers.

## Key facts extracted
- Database credentials: admin / m19RoAU0hP41A1sTsq6K
- XXE endpoint: POST to tracker_diRbPr00f314.php with base64-encoded XML
- sudo: (root) NOPASSWD: /usr/bin/python3.8 /home/development/skytrain_inc/ticketValidator.py
- Ticket validator requires ticketCode % 7 == 4 before eval execution

## Filed into
[[bountyhunter]], [[xxe]], [[php-filter-wrapper]], [[python-eval-injection]]
