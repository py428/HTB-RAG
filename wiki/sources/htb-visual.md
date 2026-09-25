---
type: source
title: "HTB Visual writeup"
raw: raw/htb-visual.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[visual]]
---
# Source: HTB Visual writeup
> 0xdf's complete writeup for HTB Visual covering the exploitation of a Visual Studio build service through pre-build event RCE, webshell deployment, and privilege escalation via FullPowers and GodPotato.

## Key facts extracted
- Exploitation path: Malicious VS project → Pre-build RCE → Webshell → FullPowers → GodPotato → SYSTEM
- Build service accepts Git URLs and compiles projects using msbuild.exe
- Pre-build commands in .csproj files execute during compilation process
- XAMPP web root writable for webshell deployment
- Local Service runs without SeImpersonate; FullPowers recovers it via scheduled task
- GodPotato exploits SeImpersonate to gain SYSTEM privileges

## Filed into
[[visual]], [[build-process-rce]], [[webshell]], [[privilege-recovery]], [[potato]]
