---
type: machine
title: Backend
platform: htb
os: linux
difficulty: medium
tags: [api, jwt, command-injection, password-reuse]
solved: 2026-07-09
sources: [[htb-backend]]
related: []
---
# Backend

> Backend is a FastAPI-based UHC box where I'll fuzz API endpoints to find registration and login, abuse mass assignment to gain admin access, forge debug-enabled JWT tokens to execute commands, and find root's password in application logs.

## Attack path
1. Enumerate [[http]] API endpoints with [[feroxbuster]] and [[wfuzz]]
2. Register account and obtain JWT token from [[jwt]]
3. Forge JWT with debug key using secret from source code
4. Execute commands via [[command-injection]] endpoint
5. Find root password in application logs (password reuse)

## Techniques used
- [[api-fuzzing]] — Discovering hidden endpoints like /api/v1/user/login and /api/v1/admin/exec
- [[mass-assignment]] — Elevating privileges by modifying is_superuser field via profile update
- [[jwt-forgery]] — Creating debug-enabled token using hardcoded signing secret
- [[command-injection]] — Executing arbitrary commands via /api/v1/admin/exec/{command}
- [[password-reuse]] — Finding root credentials in auth.log where user accidentally typed password in username field

## Tools used
[[nmap]], [[feroxbuster]], [[wfuzz]], [[curl]], [[jq]]

## Services / ports
[[ssh]] (22), [[http]] (80)

## Lessons / notes
- API fuzzing requires different strategies than web directory brute forcing
- Mass assignment vulnerabilities allow privilege escalation by injecting unexpected fields
- JWT signing secrets are often hardcoded in application source or environment variables
- User errors like typing passwords in wrong fields can leave credentials in logs
- FastAPI apps typically run with uvicorn and have auto-generated Swagger docs at /docs
