---
type: machine
title: Strutted
platform: htb
os: linux
difficulty: medium
tags: [linux, web, privesc, apache-struts, file-upload, webshell, sudo-abuse, tcpdump]
solved: 2026-07-09
sources: [[htb-strutted]]
related: []
---
# Strutted
> Apache Tomcat with vulnerable Struts framework (CVE-2024-53677), exploited via file upload parameter manipulation to upload webshell, then credential reuse and tcpdump GTFObins for root.
## Attack path
1. [[apache-struts-rce]] (CVE-2024-53677) via file upload parameter manipulation for webshell
2. [[webshell-upload]] as tomcat user using JSP webshell
3. [[password-reuse]] — Tomcat admin password works for SSH as james
4. [[gtfobins]] — tcpdump with -z flag to execute commands as root
## Techniques used
- [[apache-struts-rce]] — CVE-2024-53677 OGNL parameter manipulation for path traversal in file upload
- [[webshell-upload]] — JSP webshell upload via top.UploadFileName parameter manipulation
- [[password-reuse]] — Tomcat admin credentials (IT14d6SSP81k) work for SSH access
- [[gtfobins]] — tcpdump post-rotation command execution (-z) with privileged user (-Z)
## Tools used
- [[nmap]] — port scanning (22, 80)
- ffuf — subdomain fuzzing
- Burp Repeater — manual exploitation of CVE-2024-53677
- [[ssh]] — access with james credentials
- [[netcat]] — reverse shell
- GTFObins — tcpdump privilege escalation reference
## Services / ports
- [[ssh]] (22) — access with james credentials
- [[http]] (80) — nginx reverse proxy to Tomcat with vulnerable Struts application
## Lessons / notes
- CVE-2024-53677 allows file upload path traversal via OGNL parameter manipulation
- The "Upload" parameter name must be exactly "Upload" (capital U) for exploitation
- Tomcat manager credentials often work for other system accounts
- tcpdump -z flag can execute scripts as root when run with sudo
- Systemd NoNewPrivileges protection can prevent su even with correct password
- Tomcat application deployment locations affect webshell execution paths
