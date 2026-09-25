---
type: machine
title: Reddish
platform: htb
os: linux
difficulty: insane
tags: [linux, docker, redis, node-red, container-breakout]
solved: 2026-07-09
sources: [[htb-reddish]]
related: []
---
# Reddish
> Complex Docker environment requiring pivoting through multiple containers using Node-Red exploitation, Redis webshell, rsync abuse, and privileged container for host access.

## Attack path
1. Exploit [[node-red]] to get initial shell in container
2. Upload [[socat]] and [[nmap]] for network enumeration and pivoting
3. Use [[redis-webshell]] to write PHP webshell into shared volume
4. Exploit rsync wildcard via [[rsync-privesc]] in backup cron job
5. Access backup container via rsync and write cron for shell
6. Exploit [[privileged-container]] to mount host filesystem and get root

## Techniques used
- [[node-red]] — Created exec node with perl reverse shell flow for initial container access
- [[redis-webshell]] — Flushed database, wrote PHP shell, set dir/dbfilename and saved to www
- [[rsync-privesc]] — Created file "-e sh p.rdb" abused by rsync wildcard in cron job
- [[privileged-container]] — Mounted /dev/sda1 to /mnt to access host filesystem

## Tools used
[[nmap]], [[curl]], [[nc]], [[redis-cli]], [[socat]], [[perl]], [[meterpreter]]

## Services / ports
[[http]] (Node-Red 1880), [[redis]] (6379), [[http]] (80), [[rsync]] (873)

## Lessons / notes
- Node-Red flows can execute arbitrary commands via exec nodes
- Redis CONFIG commands allow writing arbitrary files to disk
- rsync wildcards can be abused for command execution via crafted filenames
- Privileged Docker containers have access to host devices in /dev
- Multiple Docker networks require pivoting through container chains