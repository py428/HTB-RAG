---
type: source
title: "HTB Mist writeup"
raw: raw/htb-mist.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[mist]]
---
# Source: HTB Mist writeup

> In-depth exploitation guide for Mist, an Insane-level Windows Active Directory box featuring Pluck CMS file disclosure, AMSI bypass, PetitPotam LDAP relay, shadow credentials, and ADCS ESC13 exploitation.

## Key facts extracted
- Domain: mist.htb with DC01 (192.168.100.100) and MS01 (192.168.100.101) virtual machine
- Pluck CMS 4.7.18 vulnerable to CVE-2024-9405 file disclosure in albums module
- Administrator password recovered from admin_backup.php: computer
- Windows Defender excludes C:\xampp\htdocs from scanning (AV evasion opportunity)
- LDAP signing NOT enforced on domain controller (enables relay attacks)
- Machine account quota set to 0 (prevents computer account creation)
- Shadow credential on MS01$ frequently reset (requires periodic renewal)
- Sharon.Mullard KeePass database protected with partial password: "d33ps" (from image)
- ESC13 abuse via SanitizationFileNames escape on Machine certificate template

## Filed into
[[mist]], [[file-disclosure]], [[amsi-bypass]], [[lnk-persistence]], [[shadow-credentials]], [[petitpotam]], [[ldap-relay]], [[kerberoasting]], [[s4u]], [[keePass-cracking]], [[adcs]]
