---
type: machine
title: APT
platform: htb
os: windows
difficulty: insane
tags: [windows, ad, kerberos, netntlm-v1, dcsync]
solved: 2026-07-09
sources: [[htb-apt]]
related: []
---
# APT
> Insane-difficulty Windows Domain Controller box focused on IPv6 enumeration, Kerberos password reuse attacks, and NTLMv1 downgrade exploitation via Defender and RoguePotato.

## Attack path
1. [[rpc-oxid-resolver]] to discover IPv6 address from RPC endpoint mapper
2. [[smb]] anonymous access to download AD backup zip file
3. [[dcsync]] offline from backup files to dump 2000 user hashes
4. [[kerberos-username-enumeration]] with Kerbrute to find valid user (henry.vinson)
5. [[password-reuse]] brute force with modified pyKerbrute to find working hash
6. [[winrm]] access using found credentials in registry
7. [[netntlm-v1]] capture via Defender SMB scan or RoguePotato RPC relay
8. [[dcsync]] using cracked machine account hash to get Administrator

## Techniques used
- [[rpc-oxid-resolver]] — Enumerating network interfaces via IOXIDResolver RPC interface without authentication
- [[kerberos-username-enumeration]] — Using Kerbrute over IPv6 to validate usernames against KDC
- [[password-reuse]] — Testing NTLM hashes from backup AD against current domain user
- [[netntlm-v1]] — Forcing NTLMv1 downgrade to crack machine account hash via rainbow tables
- [[dcsync]] — Using DRSUAPI to dump NTDS.dit with machine account credentials

## Tools used
- [[nmap]], [[impacket]], [[crackmapexec]], [[kerbrute]], [[evil-winrm]], [[mimikatz]], [[hashcat]], [[secretsdump]], [[responder]], [[ysoserial]]

## Services / ports
- [[rpc]] (135), [[smb]] (445), [[kerberos]] (88), [[ldap]] (389/636/3268/3269), [[winrm]] (5985/47001)

## Lessons / notes
- IPv6 addresses can be discovered via RPC even when not visible in standard scans
- Kerberos over IPv6 requires hosts file configuration for tool compatibility
- SMB brute force protection (wail2ban) requires alternative Kerberos approaches
- NTLMv1 hashes can be cracked instantly using rainbow tables at crack.sh
- Defender can be triggered to authenticate to attacker-controlled SMB shares
- DCSync requires Domain Admin or equivalent machine account permissions
