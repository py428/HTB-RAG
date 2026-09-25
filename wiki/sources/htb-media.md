---
type: source
title: "HTB Media writeup"
raw: raw/htb-media.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[media]]
---
# Source: HTB Media writeup
> Windows medium box starting with NTLM hash capture via .wax file upload, followed by junction point abuse to upload a webshell, then FullPowers and GodPotato for SYSTEM.

## Key facts extracted
- .wax file upload triggers Windows Media Player, leaking NTLM hash to Responder
- Hash cracked with hashcat: 1234virus@
- Upload system uses MD5 hash of form fields for directory names
- Junction point abuse redirects uploads to web root for webshell execution
- FullPowers restores SeImpersonatePrivilege for local service account
- GodPotato exploits impersonation privilege for SYSTEM

## Filed into
[[media]], [[ntlm-capture]], [[hash-cracking]], [[junction-point]], [[privilege-escalation]], [[godpotato]]
