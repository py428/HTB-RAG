---
type: source
title: "HTB LogForge writeup"
raw: raw/htb-logforge.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[logforge]]
---

# Source: HTB LogForge writeup
> Comprehensive Log4j exploitation guide covering Orange Tsai Tomcat bypass, JNDI injection with ysoserial, environment variable leakage, and LDAP protocol analysis.

## Key facts extracted
- Apache/Tomcat hosting requires Orange Tsai path normalization bypass (..;)
- Tomcat manager accessible with tomcat/tomcat credentials
- WAR upload disabled (1 byte limit), requiring Log4Shell exploitation
- Log4Shell achieved via JNDI LDAP injection with ysoserial CommonsCollections5
- Java FTP server on localhost uses Log4j for username logging
- Environment variables leaked via ${env:ftp_user} and ${env:ftp_password} in JNDI string
- Leaked credentials (ippsec/password) grant FTP root access and su to root

## Filed into
[[logforge]], [[orange-tsai]], [[log4shell]], [[jndi-injection]], [[ldap-injection]], [[environment-variable-leak]], [[log4j]], [[reverse-engineering]]
