---
type: source
title: "HTB RE writeup"
raw: raw/htb-re.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[re]]
---
# Source: HTB RE writeup
> Detailed writeup for the RE HackTheBox machine covering malware analysis, document macro obfuscation, archive vulnerabilities, and XXE exploitation in Ghidra project files.

## Key facts extracted
- Windows box with malware sandbox processing .ods files
- Yara rules detect Metasploit and basic PowerShell patterns
- WinRar ACE vulnerability enables directory traversal
- Ghidra project processing automation runs as coby user
- XXE in .prp files triggers authentication to capture hashes
- Multiple unintended privilege escalation paths via service abuse
- EFS-protected root.txt requires specific user credentials

## Filed into
[[re]], [[macro-obfuscation]], [[winrar-slip]], [[xxe]], [[dnsadmins-dnscmd-abuse]]
