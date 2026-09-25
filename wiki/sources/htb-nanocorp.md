---
type: source
title: "HTB NanoCorp writeup"
raw: raw/htb-nanocorp.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[nanocorp]]
---
# Source: HTB NanoCorp writeup
> Hard-difficulty Windows Active Directory box with careers portal file upload, Net-NTLMv2 capture, AD privilege escalation, and Checkmk agent exploitation.

## Key facts extracted
- Domain: nanocorp.htb with XAMPP web server hosting careers portal
- File upload functionality processed ZIP archives using Windows extraction
- CVE-2025-24071 allowed NTLM hash leak via malicious .library-ms files in archives
- Service account web_svc had ACL permissions to modify group membership
- monitoring_svc account in Protected Users group with ForceChangePassword access
- Checkmk agent 2.1 installed with CVE-2024-0670 vulnerability
- Multiple automated scripts maintained intended state including RDP session management
- LDAP signing not required enabling unintended NTLM relay attack vector

## Filed into
[[nanocorp]], [[cve-2025-24071]], [[ntlm-capture]], [[acl-genericwrite]], [[ntlm-disabled-protected-users]], [[cve-2024-0670]]