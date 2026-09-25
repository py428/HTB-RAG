---
type: machine
title: BackendTwo
platform: htb
os: linux
difficulty: medium
tags: [api, jwt, file-write, sudo]
solved: 2026-07-09
sources: [[htb-backendtwo]]
related: []
---
# BackendTwo

> BackendTwo is a FastAPI UHC box building on Backend with updated vulnerabilities. I'll enumerate the API, abuse mass assignment for admin access, read source via file read to find JWT secret, forge debug tokens for file write, backdoor the application, and bypass pam-wordle for root.

## Attack path
1. Enumerate [[http]] API endpoints with [[feroxbuster]]
2. Register account and abuse [[mass-assignment]] to gain admin privileges
3. Read application source via file read endpoint to find JWT secret
4. Forge JWT with debug key and file write capability
5. Backdoor Python application to get shell as htb user
6. Exploit sudo rule with pam-wordle bypass to gain root access

## Techniques used
- [[mass-assignment]] — Elevating to admin by injecting is_superuser field in profile update
- [[jwt-forgery]] — Creating debug-enabled token using API_KEY from environment
- [[file-write]] — Writing malicious code to Python source for code execution
- [[application-backdoor]] — Injecting shell command into Flask route handler
- [[pam-wordle-bypass]] — Reading word list from /opt/.words to cheat at Wordle game for sudo

## Tools used
[[nmap]], [[feroxbuster]], [[curl]], [[jq]], Python/jwt, [[ffuf]]

## Services / ports
[[ssh]] (22), [[http]] (80)

## Lessons / notes
- Hot reload (--reload) on uvicorn makes file write exploitation viable
- Mass assignment in profile update endpoints is a common privilege escalation vector
- Environment variables exposed via /proc/self/environ can contain JWT secrets
- pam-wordle can be bypassed by reading the word list file directly
- Word filtering with grep can efficiently solve Wordle-style challenges
