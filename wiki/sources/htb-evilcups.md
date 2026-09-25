---
type: source
title: "HTB EvilCUPS writeup"
raw: raw/htb-evilcups.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[evilcups]]
---
# Source: HTB EvilCUPS writeup

> Technical analysis of EvilCUPS Linux box covering CUPS vulnerability chain exploitation, malicious printer creation, and credential recovery from print spool files.

## Key facts extracted
- Four CVEs exploited: CVE-2024-47176 (cups-browsed), CVE-2024-47076 (libcupsfilters), CVE-2024-47175 (libppd), CVE-2024-47177 (cups-filters)
- CUPS version 2.4.2 running on Debian 12
- Exploit creates malicious printer with FoomaticRIPCommandLine injection
- Print test page triggers execution via foomatic-rip filter
- Previous print job in /var/spool/cups/d00001-001 contains password: Br3@k-G!@ss-r00t-evilcups
- PPD files stored in /etc/cups/ppd/ after printer creation

## Filed into
[[evilcups]], [[cups-rce]], [[print-job-analysis]]
