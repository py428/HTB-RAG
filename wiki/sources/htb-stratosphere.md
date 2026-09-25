---
type: source
title: "HTB Stratosphere writeup"
raw: raw/htb-stratosphere.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[stratosphere]]
---
# Source: HTB Stratosphere writeup
> Medium Linux box with Apache Tomcat and vulnerable Struts framework, exploited via CVE-2017-5638 for initial foothold, then database credential harvesting and hash cracking for user escalation, and Python2 eval injection via sudo for root access.
## Key facts extracted
- Apache Tomcat 8.5.14 running Struts application on port 80
- CVE-2017-5638 OGNL injection in Content-Type header for RCE
- MariaDB on localhost with user credentials in database
- Python2 vs Python3 input() behavior difference for privilege escalation
- sudo permissions on test.py with wildcard python* binary
## Filed into
[[stratosphere]], [[apache-struts-rce]], [[command-injection]], [[sqli]], [[hash-cracking]], [[python-eval-injection]], [[sudo-abuse]]
