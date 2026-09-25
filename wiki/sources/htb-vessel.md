---
type: source
title: "HTB Vessel writeup"
raw: raw/htb-vessel.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[vessel]]
---
# Source: HTB Vessel writeup
> Hard box combining web exploitation (Express type confusion, Open Web Analytics), reverse engineering (PyInstaller), and container escape (CRI-O).

## Key facts extracted
- Main site: Express.js with mysqljs, subdomain: Open Web Analytics (OWA) 1.7.3
- MySQL credentials: `default:daqvACHKvRn84VdVp` (not needed for exploitation)
- Git repo shows attempted SQLi fix but type confusion remains
- OWA cache files at `owa-data/caches/[user_id]/owa_user/[hash].php`
- Password generator uses weak PRNG seeding with milliseconds
- CRI-O 1.19.6 with vulnerable pinns binary (CVE-2022-0811)
- Python 3.7 PyInstaller executable requires matching version for extraction

## Filed into
[[vessel]], [[git-exposure]], [[mysqljs-type-confusion]], [[cve-2022-24637]], [[mass-assignment]], [[pyinstaller-reverse]], [[cve-2022-0811]]
