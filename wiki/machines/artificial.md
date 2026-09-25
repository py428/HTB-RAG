---
type: machine
title: Artificial
platform: htb
os: linux
difficulty: easy
tags: [ad, linux, web, privesc]
solved: 2026-07-09
sources: [[htb-artificial]]
related: []
---
# Artificial

> Easy Linux box hosting an AI model upload service running TensorFlow 2.13.1. Exploitation involves deserialization vulnerability in h5 model files for initial access, followed by database hash cracking and Backrest backup software abuse through multiple privilege escalation vectors.

## Attack path
1. [[nmap]] scan reveals [[http]] service redirecting to artificial.htb
2. Register and login to access AI model upload functionality
3. Exploit [[tensorflow-deserialization]] by uploading malicious .h5 model file
4. Extract and crack user hashes from SQLite database
5. SSH access with cracked credentials
6. [[ssh-tunnel]] to access Backrest on localhost:9898
7. Abuse Backrest backups or hooks for root access

## Techniques used
- [[tensorflow-deserialization]] — Malicious h5 model with Lambda layer executing arbitrary commands
- [[hash-cracking]] — MD5 password hash extraction and cracking
- [[ssh-tunnel]] — Local port forwarding to access internal services
- [[backup-abuse]] — Reading SSH keys from backup snapshots
- [[command-injection]] — Backrest password-command hook exploitation

## Tools used
- [[nmap]], [[docker]], [[hashcat]], [[ffuf]], [[ssh]]

## Services / ports
- 22/tcp [[ssh]] — OpenSSH 8.2p1
- 80/tcp [[http]] — nginx 1.18.0 (Flask app)
- 9898/tcp — Backrest web interface (localhost only)

## Lessons / notes
- TensorFlow model deserialization can execute arbitrary Python code during model.load()
- Building malicious models requires matching Python version and package versions exactly
- Docker files provided by targets remove version guesswork
- Backrest is a GUI wrapper around restic backup utility
- Multiple escalation paths exist in backup software (file restoration, hooks, command injection)
- Backup snapshots can contain sensitive files like SSH keys and credentials
