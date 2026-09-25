---
type: machine
title: EvilCUPS
platform: htb
os: linux
difficulty: medium
tags: [linux, cups, rce]
solved: 2026-07-09
sources: [[htb-evilcups]]
related: []
---
# EvilCUPS
> Linux box exploiting multiple CUPS vulnerabilities (CVE-2024-47176, CVE-2024-47076, CVE-2024-47175, CVE-2024-47177) to achieve RCE via malicious printer injection, with root access through print job credential recovery.

## Attack path
1. Chain of four CUPS CVEs to add malicious printer remotely
2. Trigger RCE by printing test page (invokes foomatic-rip filter)
3. [[print-job-analysis]] — Extract PostScript file from /var/spool/cups to recover root password
4. su to root with recovered password

## Techniques used
- [[cups-rce]] — Exploiting CUPS vulnerabilities to add malicious printer with injected command
- [[ipp-browse-packet]] — Sending UDP browse packet to trigger printer addition
- [[ppd-injection]] — Injecting malicious FoomaticRIPCommandLine into PPD file
- [[print-job-analysis]] — Reading PostScript files from spool directory to extract sensitive data

## Tools used
- [[nmap]], evil-cups.py (exploit script), ps2pdf

## Services / ports
- [[ssh]] (22), [[ipp]] (631)

## Lessons / notes
- CUPS (Common Unix Printing System) has multiple remote code execution vulnerabilities
- cups-browsed UDP 631 allows remote printer addition via browse packets
- PPD (PostScript Printer Description) files can be injected with malicious commands
- foomatic-rip filter is vulnerable to command injection via FoomaticRIPCommandLine
- Print jobs remain in /var/spool/cups as d#####-### files, potentially containing sensitive data
- CUPS web interface accessible on TCP 631 for printer management
- Chain of vulnerabilities: browse → libcupsfilters → libppd → cups-filters
