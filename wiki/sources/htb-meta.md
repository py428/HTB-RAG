---
type: source
title: "HTB Meta writeup"
raw: raw/htb-meta.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[meta]]
---
# Source: HTB Meta writeup
> Linux medium box focused on image processing vulnerabilities, featuring ExifTool CVE exploitation and ImageMagick command injection for user, then neofetch configuration abuse for root.

## Key facts extracted
- ExifTool version vulnerable to CVE-2021-22204 for arbitrary code execution
- DjVu file format can contain Perl code execution in metadata
- ImageMagick 7.0.10-36 vulnerable to CVE-2020-29599 command injection
- SVG/MSL polyglot files exploit ImageMagick's processing pipeline
- Cron job runs mogrify against uploaded files every minute
- Neofetch configurable via XDG_CONFIG_HOME preserved by sudo

## Filed into
[[meta]], [[exiftool-cve]], [[command-injection]], [[cronjob-hijack]], [[ssh-key-reuse]], [[configuration-escalation]]
