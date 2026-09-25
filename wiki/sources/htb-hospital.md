---
type: source
title: "HTB Hospital writeup"
raw: raw/htb-hospital.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[hospital]]
---
# Source: HTB Hospital writeup
> Detailed writeup for HTB Hospital machine covering PHP upload bypass, kernel exploitation, Windows domain compromise, Ghostscript exploitation, and multiple privilege escalation paths.

## Key facts extracted
- Target: Hospital medical company with Windows DC and Ubuntu VM webserver
- Primary attack vector: PHP upload bypass leading to container compromise, then lateral movement to Windows
- Initial foothold: Medical records upload form accepts PHP files via .phar extension bypass
- Container privilege escalation: Two kernel exploits available (CVE-2023-35001 and GameOver(lay))
- Lateral movement: Password reuse between Linux container and Windows systems
- Email exploitation: Ghostscript CVE-2023-2023-36664 exploited via malicious EPS attachments
- Multiple admin paths: Keystroke capture, RDP password theft, unintended XAMPP webshell
- Realistic automation: hMailServer scripting processes email attachments automatically

## Filed into
[[hospital]], [[file-upload-php-bypass]], [[disable-functions-bypass]], [[kernel-exploit]], [[password-cracking]], [[password-reuse]], [[command-injection]], [[keystroke-capture]], [[rdp-initial-access]], [[xss-webshell-unintended]], [[cve-2023-36664]]
