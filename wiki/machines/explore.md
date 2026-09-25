---
type: machine
title: Explore
platform: htb
os: android
difficulty: easy
tags: [android, web, file-read, adb]
solved: 2026-07-09
sources: [[htb-explore]]
related: []
---
# Explore
> Android phone with exposed file manager service allows reading credentials from images, then ADB debug bridge for root shell.

## Attack path
1. Exploit [[cve-2019-6447]] — ES File Explorer open port leaks file system access
2. Extract credentials from exfiltrated image file via [[file-read]] vulnerability  
3. SSH access with credentials, then use [[adb]] for root shell via Android Debug Bridge

## Techniques used
- [[cve-2019-6447]] — ES File Explorer file read vulnerability on port 59777
- [[file-read]] — Arbitrary file access via exposed JSON API
- [[adb]] — Android Debug Bridge for privilege escalation to root

## Tools used
- [[nmap]], [[curl]], [[sshpass]], [[adb]]

## Services / ports
- [[ssh]] (2222), [[http]] (42135), unknown services (38925, 59777)

## Lessons / notes
- Mobile vulnerabilities are often about exposed services rather than traditional exploitation
- ADB debug bridge provides straightforward root access on Android devices
- File manager applications can expose sensitive system files when network services are enabled