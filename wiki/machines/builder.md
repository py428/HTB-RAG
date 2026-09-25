---
type: machine
title: Builder
platform: htb
os: linux
difficulty: medium
tags: [linux, jenkins, cve-2024-23897, file-read, hash-cracking, ssh-key, privesc]
solved: 2026-07-09
sources: [[htb-builder]]
related: []
---
# Builder
> Medium Linux box focused on recent Jenkins vulnerability CVE-2024-23897 allowing partial file read through CLI interface. Initial access through reading Jenkins user config with bcrypt hash, cracking password to access web interface, then recovering SSH keys through Jenkins credential storage or SSH agent plugin. Root access achieved using recovered SSH keys.

## Attack path
1. [[jenkins-cli-file-read]] — Exploit CVE-2024-23897 for partial file read via @/filepath syntax
2. [[hash-cracking]] — Extract and crack bcrypt hash from Jenkins user config
3. [[jenkins-authentication]] — Authenticate as jennifer with cracked password "princess"
4. [[ssh-key-recovery]] — Recover root SSH key via Jenkins credential dump or SSH agent
5. [[ssh-access]] — SSH as root using recovered private key

## Techniques used
- [[jenkins-cli-file-read]] — CVE-2024-23897 arbitrary file read through Jenkins CLI @filepath feature
- [[hash-cracking]] — Bcrypt hash cracking with hashcat mode 3200
- [[jenkins-authentication]] — Jenkins web interface access with cracked credentials
- [[ssh-key-recovery]] — Jenkins credential storage and SSH agent plugin for key extraction
- [[ssh-access]] — Root SSH access using recovered private key

## Tools used
[[nmap]], wget, java, python, hashcat, ssh, python, groovy

## Services / ports
[[ssh]] (22), [[http]] (8080 - Jenkins)

## Lessons / notes
- Jenkins CLI accepts @/filepath syntax to read file contents as arguments
- Different CLI commands return different amounts of data (reload-node returned 19 lines)
- Jenkins stores user bcrypt hashes in config.xml files in users/ directory
- Jenkins credentials can be dumped via Groovy script console or used via SSH agent plugin
- SSH agent plugin allows running commands on remote system with stored SSH keys
- Root SSH key was stored in Jenkins credential store for deployment purposes
