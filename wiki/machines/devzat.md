---
type: machine
title: Devzat
platform: htb
os: linux
difficulty: medium
tags: [linux, web, go, influxdb, ssh, command-injection]
solved: 2026-07-09
sources: [[htb-devzat]]
related: []
---
# Devzat
> Chat-over-SSH application with multiple attack surfaces: command injection in Go pet inventory API, InfluxDB authentication bypass for user credential extraction, and file read vulnerability in development chat server for root SSH key exfiltration.

## Attack path
1. [[git-repo-exposure]] — Download exposed .git directory from pets.devzat.htb
2. [[command-injection]] — Inject commands via species parameter in pet addition API
3. [[cve-2019-20933]] — Exploit InfluxDB JWT authentication bypass with empty secret
4. [[file-read]] — Use /file command in dev chat instance to read root SSH key
5. [[ssh]] — Authenticate with exfiltrated root private key

## Techniques used
- [[git-repo-exposure]] — Directory listing enabled on .git allows full source download with wget
- [[command-injection]] — Go exec.Command with unsanitized species parameter enables shell injection
- [[cve-2019-20933]] — InfluxDB 1.7.5 accepts JWT with empty shared secret for authentication bypass
- [[jwt-forgery]] — Craft JWT with empty HMAC to authenticate as admin user
- [[file-read]] — Development chat server /file command vulnerable to path traversal
- [[ssh]] — Private key authentication provides direct root shell access

## Tools used
[[nmap]], [[wfuzz]], [[feroxbuster]], [[wget]], [[git]], [[curl]], [[netcat]], [[ssh]], [[python]], [[tcpdump]]

## Services / ports
- [[ssh]] (22) — OpenSSH 8.2p1 Ubuntu
- [[ssh]] (8000) — Devzat chat server (Go-based)
- [[http]] (80) — Apache 2.4.41
- InfluxDB (8086) — localhost only

## Lessons / notes
- Exposed .git directories with directory listing enable full source recovery
- Go exec.Command with user input requires careful validation to prevent command injection
- InfluxDB JWT authentication bypass works when shared secret configuration is empty
- Chat application user "reservation" suggests localhost-only access mechanisms
- Development instances may have different vulnerabilities than production versions
- Path traversal in file read functions can expose sensitive files like SSH keys
