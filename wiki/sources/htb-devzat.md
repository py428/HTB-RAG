---
type: source
title: "HTB Devzat writeup"
raw: raw/htb-devzat.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[devzat]]
---
# Source: HTB Devzat writeup
> Multi-vector exploitation of chat-over-SSH application combining web application security (git exposure, command injection), database auth bypass, and local privilege escalation through development instance vulnerabilities.

## Key facts extracted
- pets.devzat.htb exposes .git directory with directory listing enabled
- Go pet shop server vulnerable to command injection via species parameter
- InfluxDB 1.7.5 running on localhost port 8086 vulnerable to CVE-2019-20933
- InfluxDB contains devzat database with user table storing passwords in plaintext
- Development chat server on localhost:8443 has /file command with path traversal vulnerability
- Root SSH key readable via /file command with password "CeilingCatStillAThingIn2021?"

## Filed into
[[devzat]], [[git-repo-exposure]], [[command-injection]], [[cve-2019-20933]], [[jwt-forgery]], [[file-read]], [[influxdb]]
