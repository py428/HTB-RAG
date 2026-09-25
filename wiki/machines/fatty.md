---
type: machine
title: Fatty
platform: htb
os: linux
difficulty: insane
tags: [linux, java, web, privesc]
solved: 2026-07-09
sources: [[htb-fatty]]
related: []
---
# Fatty
> An insane difficulty Java thick client box requiring extensive reverse engineering and modification of a JAR client to exploit SQL injection, directory traversal, and Java deserialization vulnerabilities in the server, then abusing SCP log file transfers to gain root access.
## Attack path
1. Download fatty-client.jar from anonymous [[ftp]]
2. Decompile and modify JAR to update server port (beans.xml) and remove signing
3. Use modified client to perform directory traversal and download fatty-server.jar
4. Analyze server JAR to find [[sqli]] in login function
5. Bypass login as admin using SQL injection to manipulate role field
6. Exploit Java deserialization in changePW function using [[ysoserial]] with CommonsCollections2 gadget
7. Get shell in container, then use [[suid-binary]] privesc technique to overwrite root's SSH authorized_keys via SCP log archival process
## Techniques used
- [[jar-modification]] — Decompile JAR with procyon, modify configuration, recompile, and repackage without signing
- [[sqli]] — SQL injection in login query to manipulate user role field for privilege escalation
- [[directory-traversal]] — Path traversal in file operations to access arbitrary files
- [[java-deserialization]] — ysoserial payload in changePW function using CommonsCollections2 gadget
- [[log-file-poisoning]] — Abuse SCP log archival process to write to root's authorized_keys via symlink race
## Tools used
- [[nmap]], [[ftp]], [[java]], [[procyon]], [[ysoserial]]
- [[curl]], [[netcat]], [[socat]], [[pspy]]
## Services / ports
- 21/tcp — [[ftp]] — vsftpd 3.0.3 with anonymous access
- 22/tcp — [[ssh]] — OpenSSH 7.4p1 Debian
- 1337-1339/tcp — Custom Java application (SSL wrapped)
## Lessons / notes
- Java JAR files can be decompiled, modified, and repackaged by removing signature files (*.SF, *.RSA)
- Spring Framework beans.xml contains application configuration including connection details
- SQL injection can manipulate database fields beyond authentication (e.g., role)
- ysoserial CommonsCollections2 provides reliable RCE via Java deserialization
- SCP file transfers can be abused for privilege escalation when combined with predictable file archival patterns
