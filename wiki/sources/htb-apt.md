---
type: source
title: "HTB APT writeup"
raw: raw/htb-apt.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[apt]]
---
# Source: HTB APT writeup
> Comprehensive walkthrough of an insane-difficulty Windows Domain Controller box requiring IPv6 enumeration, Kerberos password reuse attacks, and NTLMv1 exploitation.

## Key facts extracted
- APT is a Windows Server 2016 Domain Controller (htb.local) accessible via IPv6
- RPC IOXIDResolver reveals IPv6 addresses not visible in standard scans
- Anonymous SMB share contains encrypted AD backup with ntds.dit and registry hives
- Only 3 of 2000 backup users exist in current domain; henry.vinson is common
- Password reuse tested via modified pyKerbrute to brute force hashes against single user
- Registry access yields henry.vinson_adm credentials for WinRM access
- NTLMv1 enabled (lmcompatibilitylevel = 2) allows machine account hash cracking
- Two paths to NTLMv1: Defender SMB scan trigger or RoguePotato RPC relay
- cracked.sh rainbow tables instantly crack NTLMv1 with specific challenge
- Machine account hash enables DCSync for Domain Admin credentials

## Filed into
[[apt]], [[rpc-oxid-resolver]], [[kerberos-username-enumeration]], [[password-reuse]], [[netntlm-v1]], [[dcsync]], [[winrm]]
