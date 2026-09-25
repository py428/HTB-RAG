---
type: machine
title: Arkham
platform: htb
os: windows
difficulty: medium
tags: [windows, web, java, deserialization, uac-bypass]
solved: 2026-07-09
sources: [[htb-arkham]]
related: []
---
# Arkham
> Medium Windows box involving LUKS encryption cracking, JavaServer Faces ViewState deserialization, and UAC bypass techniques for privilege escalation.

## Attack path
1. [[smb]] enumeration yields encrypted backup image
2. LUKS brute force with theme-based wordlist
3. Extract JSF configuration with encryption keys from mounted image
4. [[deserialization]] via ViewState manipulation with ysoserial payload
5. Email file analysis reveals Batman user credentials
6. [[uac-bypass]] using CMSTP or SystemPropertiesAdvanced for SYSTEM access

## Techniques used
- [[luks-brute-force]] — Theme-based wordlist cracking with bruteforce-luks
- [[deserialization]] — JSF ViewState exploitation with DES encryption and HMAC signing
- [[uac-bypass]] — CMSTP DLL hijacking and SystemPropertiesAdvanced techniques
- [[file-format-exploitation]] — OST email file parsing with readpst

## Tools used
- [[nmap]], [[smbclient]], [[bruteforce-luks]], [[cryptsetup]], [[ysoserial]], [[readpst]], [[hashcat]], [[msfconsole]]

## Services / ports
- [[http]] (80 IIS, 8080 Tomcat), [[smb]] (445), [[rpc]] (135)

## Lessons / notes
- LUKS encryption slow to brute force but vulnerable to themed wordlists
- JSF ViewState encryption requires manual implementation due to non-standard defaults
- Multiple ysoserial payloads needed; CommonsCollections5 works with DES encryption
- Email OST files contain recoverable credentials and attachments
- UAC bypass techniques require DLL compilation or specific executable paths
- CMSTP bypass works well with process migration in Meterpreter
- Constrained Language Mode can be bypassed with PSByPassCLM or Meterpreter
