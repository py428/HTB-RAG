---
type: source
title: "HTB Kotarak writeup"
raw: raw/htb-kotarak.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[kotarak]]
---
# Source: HTB Kotarak writeup
> Comprehensive 0xdf writeup covering SSRF enumeration, Tomcat exploitation, NTDS credential dumping, and wget vulnerability exploitation for container root access, plus alternative disk group privilege escalation.

## Key facts extracted
- Ubuntu 16.04 with Tomcat 8.5.5 and custom web browser service on port 60000
- SSRF used to enumerate localhost ports and discover Tomcat backup file with credentials
- Exfiltrated ntds.dit and SYSTEM hive from old pentest data in /home/tomcat/to_archive/
- CVE-2016-4971 exploited via wget cron job in container using FTP redirect to write .wgetrc and cron file
- Alternative root path via disk group access to read LVM device (/dev/dm-0) and mount container filesystem

## Filed into
[[kotarak]], [[ssrf]], [[tomcat-war-upload]], [[dcsync]], [[wget-cve-2016-4971]], [[disk-group-abuse]]
