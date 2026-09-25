---
type: machine
title: Unobtainium
platform: htb
os: linux
difficulty: hard
tags: [linux, web, kubernetes, container, hard]
solved: 2026-07-09
sources: [[htb-unobtainium]]
related: []
---
# Unobtainium
> Hard Kubernetes box featuring an Electron chat application with prototype pollution, command injection via npm package, and container escape through malicious pod with host filesystem mount.

## Attack path
1. [[local-file-include]] via `/todo` endpoint to read server source code
2. [[prototype-pollution]] via `PUT /` endpoint to gain `canUpload` privilege
3. [[command-injection]] via `/upload` endpoint abusing vulnerable `google-cloudstorage-commands` npm package
4. [[kubernetes-token-abuse]] - use service account token to enumerate pods and escalate to admin
5. [[container-escape]] - create malicious pod with host filesystem mounted to get root on host

## Techniques used
- [[local-file-inclusion]] — File read vulnerability in `/todo` endpoint allows reading server-side JavaScript source code
- [[prototype-pollution]] — lodash merge vulnerability in message creation allows adding `canUpload` property to user object
- [[command-injection]] — `google-cloudstorage-commands` npm package (deprecated) passes filename directly to `exec()` for gsutil command
- [[kubernetes-token-abuse]] — Service account token in `/run/secrets/kubernetes.io/serviceaccount/token` allows pod enumeration and privilege escalation to cluster admin
- [[container-escape]] — Creating malicious pod with host filesystem volume mount provides root access to host filesystem

## Tools used
- [[nmap]] — port scanning and service detection
- [[curl]] — API interaction and testing
- feroxbuster — directory brute forcing
- npm/asar — Electron app unpacking
- kubectl — Kubernetes cluster management

## Services / ports
- [[ssh]] — 22/tcp
- [[http]] — 80/tcp (Apache, chat application)
- [[https]] — 8443/tcp (Kubernetes API server)
- etcd-client — 2379/tcp
- etcd-server — 2380/tcp
- zabbix-agent — 10050/tcp
- zabbix-trapper — 10051/tcp

## Lessons / notes
- Electron applications can be unpacked using asar to view source code
- Prototype pollution in lodash merge can modify object properties globally
- Deprecated npm packages often have security vulnerabilities
- Kubernetes service account tokens can provide significant privileges
- Pods can mount host filesystems for container escape
- Git repositories exposed on web servers can be dumped with git-dumper
