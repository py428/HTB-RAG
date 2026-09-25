---
type: source
title: "HTB Pterodactyl writeup"
raw: raw/htb-pterodactyl.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[pterodactyl]]
---

# Source: HTB Pterodactyl writeup

> Complete writeup for HTB Pterodactyl covering CVE-2025-49132 exploitation, PTERODACTYL panel abuse, Active Directory enumeration, and openSUSE privilege escalation via Polkit bypass and udisks XFS filesystem abuse.

## Key facts extracted

- **Initial Access**: Unauthenticated directory traversal in Pterodactyl Panel v1.11.10 (CVE-2025-49132) via locale.json endpoint
- **RCE Method**: PEAR pearcmd.php abuse with register_argc_argv for LFI-to-RCE chain
- **Database Creds**: pterodactyl / PteraPanel from config/database.php
- **User Pivot**: phileasfogg3 password !QAZ2wsx from cracked bcrypt hash
- **Privesc Chain**: CVE-2025-6018 (PAM bypass) + CVE-2025-6019 (udisks abuse) for root
- **Target OS**: openSUSE Leap 15.6 with non-standard sudo configuration

## Filed into

[[pterodactyl]], [[directory-traversal]], [[lfi-to-rce]], [[hash-cracking]], [[password-reuse]], [[polkit-bypass]], [[udisks-abuse]], [[suid-binary]]
