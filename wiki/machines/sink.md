---
type: machine
title: Sink
platform: htb
os: linux
difficulty: insane
tags: [web, aws, cloud, privesc]
solved: 2026-07-09
sources: [[htb-sink]]
related: []
---
# Sink
> Insane-difficulty Linux box featuring HTTP request smuggling (CVE-2019-18277) between HAProxy and Gunicorn to leak admin cookies, then exploiting AWS LocalStack services (Secrets Manager, KMS) to find credentials and decrypt data for root access.

## Attack path
1. [[http-request-smuggling]] to leak admin session cookie via crafted request to /notes endpoint
2. [[aws-secrets-manager]] enumeration to find david@sink.htb credentials
3. [[aws-kms-decrypt]] to decrypt servers.enc file containing admin password
4. SSH as root using decrypted admin password

## Techniques used
- [[http-request-smuggling]] — Exploited mismatch in Transfer-Encoding header handling between HAProxy 1.9.10 and Gunicorn 20.0.0 to capture admin JWT via /notes endpoint poisoning
- [[aws-secrets-manager]] — Enumerated and extracted credentials using awslocal CLI, found david@sink.htb password in Jira Support secret
- [[aws-kms-decrypt]] — Used KMS decrypt with key 804125db-bdf1-465a-a058-07fc87c0fad0 and RSAES_OAEP_SHA_256 algorithm to decrypt gzipped tar archive containing admin credentials
- [[git-privkey-enum]] — Found SSH private key in Gitea Key_Management repository commit history for marcus user

## Tools used
- [[nmap]] for port and service discovery
- [[curl]] for HTTP testing and request smuggling
- [[awslocal]] (aws CLI) for AWS LocalStack interaction
- [[socket]] (Python) for crafting raw HTTP smuggling packets
- [[base64]] and [[tar]] and [[zcat]] for decrypting KMS output
- [[ssh]] for access

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 8.2p1 Ubuntu
- 3000/tcp — [[http]] — Gitea (Git hosting)  
- 5000/tcp — [[http]] — Python Flask app behind HAProxy

## Lessons / notes
- Request smuggling relies on front-end and back-end parsing HTTP request boundaries differently — here HAProxy honors Content-Length while Gunicorn processes Transfer-Encoding with vertical tab bypass
- AWS LocalStack exposes production-like APIs on localhost:4566, requiring endpoint URL specification for all awslocal commands
- KMS keys with ENCRYPT_DECRYPT usage can decrypt files if the correct encryption algorithm is specified
- Docker container scaling (16 instances) with iptables load balancing allows multiple players to exploit race conditions simultaneously
- The /etc/exports NFS configuration with no_subtree_check enabled filesystem escape from shares