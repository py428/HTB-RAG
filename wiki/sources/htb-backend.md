---
type: source
title: "HTB Backend writeup"
raw: raw/htb-backend.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[backend]]
---
# Source: HTB Backend writeup

> Detailed writeup for HackTheBox machine Backend covering API enumeration, JWT token manipulation, and privilege escalation through credential discovery in application logs.

## Key facts extracted
- FastAPI application with endpoints at /api/v1/user/login, /api/v1/user/signup, /api/v1/admin/exec/{command}
- JWT signing secret: "SuperSecretSigningKey-HTB" found in app/core/config.py
- Root password "Tr0ub4dor&3" discovered in auth.log where accidentally typed as username
- Debug privilege enabled by adding "debug": true to JWT payload before re-encoding

## Filed into
[[backend]], [[api-fuzzing]], [[mass-assignment]], [[jwt-forgery]], [[command-injection]], [[password-reuse]]
