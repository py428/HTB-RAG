---
type: machine
title: Squashed
platform: htb
os: linux
difficulty: easy
tags: [nfs, web, linux, privesc]
solved: 2026-07-09
sources: [[htb-squashed]]
related: []
---
# Squashed
> Easy Linux box featuring NFS misconfigurations. Initial foothold through exploiting NFS share permissions with userid spoofing to upload a webshell. Privilege escalation via X11 magic cookie theft to screenshot a KeePassXC password manager revealing the root password.
## Attack path
1. [[nfs-enumeration]] — discover exported shares for `/home/ross` and `/var/www/html`
2. [[userid-spoofing]] — create local user with matching UID (2017) to access web root
3. [[web-shell-upload]] — upload PHP webshell to writable NFS mount
4. [[x11-cookie-theft]] — steal `.Xauthority` cookie from NFS share
5. [[x11-screenshot]] — use `xwd` to capture desktop screenshot via X11
6. [[credential-theft]] — extract root password from KeePassXC in screenshot

## Techniques used
- [[nfs-enumeration]] — enumerate NFS shares with `showmount -e`
- [[userid-spoofing]] — create local user matching NFS UID/GID to bypass permissions
- [[web-shell-upload]] — upload PHP webshell to gain execution
- [[x11-cookie-theft]] — extract X11 authorization cookie from NFS mount
- [[x11-screenshot]] — capture user desktop screenshot using X11 tools
- [[credential-theft]] — obtain password from password manager screenshot

## Tools used
- [[nmap]] — port scanning and service enumeration
- [[showmount]] — NFS share enumeration
- mount — mount NFS shares locally
- feroxbuster — directory brute force
- [[curl]] — web requests and file transfer
- [[nc]] — reverse shell listener
- xwd — X11 window dump for screenshots
- ImageMagick — image format conversion

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 80/tcp — [[http]] — Apache 2.4.41
- 111/tcp — rpcbind
- 2049/tcp — [[nfs]] — NFS exports
- 41527/tcp — nlockmgr
- 43109/tcp — mountd
- 57809/tcp — mountd
- 58777/tcp — mountd

## Lessons / notes
- NFS uses UID/GID numbers, not names — matching local UIDs grants access
- X11 cookies (`.Xauthority`) can be stolen and used remotely
- KeePassXC screenshots may contain visible passwords
- Web directories on NFS are often writable for deployment
- Multiple RPC services support NFS operations
