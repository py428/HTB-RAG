---
type: source
title: "HTB Scavenger writeup"
raw: raw/htb-scavenger.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[scavenger]]
---
# Source: HTB Scavenger writeup
> Comprehensive writeup covering enumeration of multiple domains and subdomains through SQL injection in whois and DNS zone transfers, finding a defaced site with webshell, credential harvesting via FTP, and root through either kernel module rootkit reverse engineering or Exim CVE-2019-10149 exploitation.

## Key facts extracted
- SQL injection in whois service (TCP 43) reveals domain list
- DNS zone transfers on multiple domains provide subdomain enumeration  
- Defaced WordPress site (sec03.rentahacker.htb) contains webshell (shell.php)
- Email credentials provide FTP access (ib01ftp:YhgRt56_Ta)
- FTP as ib01c01 contains user.txt and rootkit kernel module (root.ko)
- Rootkit analysis shows modified magic string "g3tPr1v" vs default "g0tR0ot"
- Alternative root via Exim CVE-2019-10149 RCE
- iptables rules block reverse shells but allow ICMP/established connections

## Filed into
[[scavenger]], [[sqli]], [[dns-zone-transfer]], [[webshell]], [[kernel-module-abuse]], [[cve-2019-10149]]
