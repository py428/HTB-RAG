---
type: machine
title: "HTB Perfection"
platform: htb
os: linux
difficulty: easy
tags: [web, linux, privesc]
solved: 2026-07-09
sources: [[htb-perfection]]
related: []
---
# HTB Perfection
> Ruby grade calculator with SSTI vulnerability requiring newline injection to bypass filters, then hash cracking for database credentials leading to root via sudo.

## Attack path
1. Enumerate [[http]] service with [[nmap]] and [[feroxbuster]]
2. Bypass input filter using [[newline-injection]] to inject special characters
3. Exploit [[ssti]] in Ruby ERB template to get RCE as susan user
4. Extract SQLite database with password hashes and cracking hints
5. Crack SHA256 hashes using [[hashcat]] with custom mask based on password format
6. Use cracked password for [[sudo]] to get root shell

## Techniques used
- [[newline-injection]] — Bypass Ruby regex filters by injecting URL-encoded newlines (%0a) to break malicious character detection across lines
- [[ssti]] — Ruby ERB template injection in grade calculation form using <%= %> syntax with IO.popen() for command execution
- [[hash-cracking]] — Custom hashcat masks for password format: {firstname}_{firstname_backwards}_{random_int}
- [[password-reuse]] — Database password reused for user sudo access

## Tools used
- [[nmap]] — Port scanning and service detection
- [[feroxbuster]] — Directory brute forcing
- [[ffuf]] — Fuzzing blocked characters and filter bypass testing
- [[hashcat]] — Cracking SHA256 hashes with custom mask attacks

## Services / ports
- [[ssh]] (22) — OpenSSH 8.9p1 Ubuntu
- [[http]] (80) — nginx + WEBrick 1.7.0 (Ruby/3.0.2) + Sinatra framework

## Lessons / notes
- Ruby regex /^[a-zA-Z0-9\/ ]+$/ doesn't match across newlines, allowing bypass with %0a
- ERB templating engine executes Ruby code in <%= %> blocks
- Custom hashcat masks: ?d for digits, ?l for lowercase, ?u for uppercase
- Default password format patterns: {name}_{reverse_name}_{random_number}
