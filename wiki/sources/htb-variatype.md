---
type: source
title: "HTB VariaType writeup"
raw: raw/htb-variatype.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[variatype]]
---
# Source: HTB VariaType writeup
> Multi-chain exploitation starting with Git exposure, combining directory traversal, multiple CVEs (fonttools, FontForge, setuptools), and cron abuse for complete system compromise.

## Key facts extracted
- Portal site: PHP with exposed `.git` repository at `/dev/.git`
- Git credentials: `gitbot:G1tB0t_Acc3ss_2025!`
- Main site: Flask app with fonttools variable font generation
- File read via `download.php` with single-pass `../` filter
- fonttools 4.50.0 vulnerable to arbitrary file write (CVE-2025-66034)
- FontForge 20230101 processes fonts via cron, vulnerable to command injection (CVE-2024-25082)
- setuptools 78.1.0 has path traversal vulnerability (CVE-2025-47273)
- `sudo` rule: `(root) NOPASSWD: /usr/bin/python3 /opt/font-tools/install_validator.py *`

## Filed into
[[variatype]], [[git-exposure]], [[directory-traversal]], [[cve-2025-66034]], [[cve-2024-25082]], [[cve-2025-47273]], [[cronjob-hijack]]
