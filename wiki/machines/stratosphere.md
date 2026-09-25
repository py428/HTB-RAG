---
type: machine
title: Stratosphere
platform: htb
os: linux
difficulty: medium
tags: [linux, web, privesc, apache-struts, rce, sqli, hash-cracking, python-eval, sudo-abuse]
solved: 2026-07-09
sources: [[htb-stratosphere]]
related: []
---
# Stratosphere
> Apache Tomcat running vulnerable Struts framework, exploited via CVE-2017-5638 RCE to get tomcat8 user, then database access and hash cracking for user escalation, finally abusing Python script with sudo via Python2 eval injection for root.
## Attack path
1. [[apache-struts-rce]] (CVE-2017-5638) for initial shell as tomcat8
2. [[command-injection]] via mkfifo shell building technique
3. [[sqli]] — accessing MariaDB with found credentials to dump user hashes
4. [[hash-cracking]] with John to crack richard's password
5. [[python-eval-injection]] — sudo test.py uses Python2 input() = eval() for root
## Techniques used
- [[apache-struts-rce]] — CVE-2017-5638 OGNL injection in Content-Type header for code execution
- [[command-injection]] — Building stable shell via mkfifo pipes and Struts RCE
- [[sqli]] — Direct MariaDB access with found credentials to dump password hashes
- [[hash-cracking]] — John the Ripper to crack SHA-256 password hashes
- [[python-eval-injection]] — Python2 input() equals eval(), allowing code execution in sudo script
## Tools used
- [[nmap]] — port scanning (22, 80, 8080)
- [[gobuster]] — directory brute force
- python — Struts exploit and shell building
- [[john]] — password hash cracking
- [[mysql]] — database access and queries
- [[netcat]] — reverse shell
## Services / ports
- [[ssh]] (22) — access with richard's credentials
- [[http]] (80) — Apache Tomcat with vulnerable Struts application
- http-proxy (8080) — Tomcat monitoring interface
- mysql (3306) — localhost only MariaDB with user credentials
## Lessons / notes
- Apache Struts OGNL injection via Content-Type header for RCE
- Python2 input() is equivalent to eval(input), allowing code execution
- Building stable shells through named pipes when direct shell access fails
- Tomcat configuration files often contain credentials in plain text
- MariaDB access often provides credential storage in web applications
