---
type: source
title: "HTB Lame writeup"
raw: raw/htb-lame.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[lame]]
---
# Source: HTB Lame writeup
> Brief walkthrough of Lame, the first HTB box released and one of the easiest. The writeup covers reconnaissance, the (non-functional) VSFTPD backdoor, and exploiting the Samba username map script vulnerability to gain immediate root access.

## Key facts extracted
- **Samba version**: 3.0.20-Debian vulnerable to CVE-2007-2447 username map script command execution
- **VSFTPD backdoor**: Version 2.3.4 present but firewall blocks port 6200 externally
- **Anonymous SMB**: /tmp share accessible via smbmap and smbclient with legacy protocol support
- **Exploit simplicity**: No authentication required—username with shell metacharacters yields immediate root
- **Multiple attack vectors**: Manual exploitation, Python script, or Metasploit all effective

## Filed into
[[lame]], [[samba-usermap-script]], [[reverse-shell]]