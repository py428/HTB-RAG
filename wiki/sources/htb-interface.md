---
type: source
title: "HTB Interface writeup"
raw: raw/htb-interface.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[interface]]
---
# Source: HTB Interface writeup
> Detailed writeup for HTB Interface machine covering DomPDF RCE exploitation and bash script privilege escalation via arithmetic expression injection.

## Key facts extracted
- Target runs Ubuntu 18.04 with nginx and Next.js framework
- Main attack surface on prd.m.rendering-api.interface.htb subdomain
- /api/html2pdf endpoint uses DomPDF 1.2.0 with font caching vulnerability
- cleanup script cleancache.sh runs as root every 2 minutes
- exiftool used to process files in /tmp with vulnerable comparison syntax

## Filed into
[[interface]], [[dompdf-rce]], [[arithmetic-expression-injection]]