---
type: source
title: "HTB MetaTwo writeup"
raw: raw/htb-metatwo.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[metatwo]]
---
# Source: HTB MetaTwo writeup
> Linux easy box featuring WordPress BookingPress SQL injection, XXE for file reading, FTP credential discovery, and Passpie password manager exploitation for root.

## Key facts extracted
- BookingPress plugin has unauthenticated SQL injection in category_id parameter
- WordPress 5.6.2 vulnerable to XXE via media upload (CVE-2021-29447)
- wp-config.php contains database and FTP credentials
- FTP server contains PHPMailer scripts with SMTP credentials
- SMTP credentials (jnelson) work for SSH access
- Passpie password manager protected by crackable PGP key

## Filed into
[[metatwo]], [[sqli]], [[wordpress-exploitation]], [[xxe]], [[ftp-access]], [[password-cracking]], [[password-manager]]
