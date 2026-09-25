---
type: source
title: "HTB Unicode writeup"
raw: raw/htb-unicode.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[unicode]]
---
# Source: HTB Unicode writeup
> Comprehensive guide to unicode normalization bypass, JWT abuse, and PyInstaller parameter injection.

## Key facts extracted
- JWT uses RS256 with jku header pointing to http://hackmedia.htb/static/jwks.json
- Open redirect at /redirect/?url= can be abused for jku bypass
- Unicode character U+2025 (‥) normalizes to "../" for directory traversal
- Database credentials: code/B3stC0d3r2021@@! from db.yaml
- treport PyInstaller binary vulnerable to parameter injection in download function
- curl parameter injection allows arbitrary file write via -o flag

## Filed into
[[unicode]], [[jwt-abuse]], [[unicode-normalization]], [[directory-traversal]], [[parameter-injection]]
