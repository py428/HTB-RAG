---
type: machine
title: Sandworm
platform: htb
os: linux
difficulty: medium
tags: [linux, web, ssti, pgp, jail, privesc, ad]
solved: 2026-07-09
sources: [[htb-sandworm]]
related: []
---
# Sandworm

> Secret spy agency website with PGP encryption demos vulnerable to SSTI in the signature verification, leading to a shell in a Firejail jail, with credentials in httpie config and a cron-job Rust code hijack for jail escape, finally exploiting CVE-2022-31214 in Firejail for root.

## Attack path

1. [[ssti]] — Server-side template injection in PGP signature verification demo
2. [[jail-escape]] — Escape Firejail jail via httpie credentials and Rust code hijack
3. [[cve-2022-31214]] — Exploit Firejail vulnerability for root access

## Techniques used

- [[ssti]] — Jinja2 template injection in PGP signature verification using crafted GPG key username
- [[jail-escape]] — Break out of Firejail jail by hijacking cargo cron job to run code as atlas
- [[cargo-hijack]] — Modify `/opt/crates/logger/src/lib.rs` to execute commands when cron builds tipnet
- [[cve-2022-31214]] — Firejail join functionality exploit for privilege escalation

## Tools used

- [[nmap]] — Port scanning
- [[feroxbuster]] — Directory brute force
- [[gpg]] — PGP key generation, encryption, and signing
- [[curl]] — HTTP client
- [[mysql]] — Database access
- [[pspy]] — Process monitoring for cron jobs
- firejoin.py — CVE-2022-31214 exploit script

## Services / ports

- [[ssh]] — 22/tcp
- [[http]] — 80/tcp — Redirects to HTTPS
- [[https]] — 443/tcp — Flask PGP encryption/decryption service

## Lessons / notes

- SSTI payload in GPG key username: `{{ namespace.__init__.__globals__.os.popen('id').read() }}`
- Firejail restricts available binaries but allows Python3 and bash
- httpie config at `~/.config/httpie/sessions/localhost_5000/admin.json` contained credentials
- Cron job runs `cargo run --offline` every two minutes as atlas user
- Silentobserver credentials: `quietLiketheWind22`
- Atlas database credentials: `GarlicAndOnionZ42`
- CVE-2022-31214 works by creating symlink at `/run/firejail/mnt/join` pointing to exploit-controlled file
