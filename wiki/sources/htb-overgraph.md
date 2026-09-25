---
type: source
title: "HTB Overgraph writeup"
raw: raw/htb-overgraph.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[overgraph]]
---

# Source: HTB Overgraph writeup
> Comprehensive writeup for HackTheBox Overgraph machine detailing reflective XSS exploitation, client-side template injection (CSTI), cross-site request forgery (CSRF), FFmpeg arbitrary file read, and binary exploitation for privilege escalation.

## Key facts extracted
- Linux system (Ubuntu 20.04) with nginx reverse proxy to multiple web applications
- Reflective XSS vulnerability in redirect parameter using JavaScript URL protocol
- Angular application with GraphQL API requiring multi-step exploitation chain
- Client-side template injection in Angular framework using {{constructor.constructor()}} syntax
- FFmpeg arbitrary file read vulnerability via concat and subfile protocols
- Binary exploitation of nreport service using heap manipulation and arbitrary file write
- Docker environment with multiple containers requiring network pivoting
- Complex multi-step attack chain requiring careful enumeration and exploitation

## Filed into
[[overgraph]], [[xss]], [[csrf]], [[csti]], [[ssti]], [[ffmpeg-arbitrary-file-read]], [[binary-exploitation]]
