---
type: source
title: "HTB Tabby writeup"
raw: raw/htb-tabby.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[tabby]]
---
# Source: HTB Tabby writeup
> Easy Linux box featuring Tomcat server and PHP website with LFI vulnerability. Leak Tomcat credentials via local file inclusion, deploy malicious WAR file using Tomcat manager API, crack backup zip password for user access, then exploit LXD group membership for privilege escalation.

## Key facts extracted
- LFI in news.php?file parameter allows reading arbitrary files
- Tomcat credentials: tomcat / $3cureP4s5w0rd123! (from tomcat-users.xml)
- Tomcat user has admin-gui and manager-script roles
- Backup zip protected with password: admin@it (cracked from rockyou.txt)
- ash user is member of lxd (116) group
- m0noc's 656-byte base64 LXD image for faster container deployment
- LXC privileged container mount: source=/ path=/mnt/root

## Filed into
[[tabby]], [[lfi]], [[tomcat-war-deployment]], [[password-cracking]], [[password-reuse]], [[lxd-container-abuse]]