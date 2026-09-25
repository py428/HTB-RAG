---
type: technique
title: Directory traversal
tags: [web, linux, windows, file-read, path-traversal, lfi]
platforms: [linux, windows]
updated: 2026-07-09
---

# Directory traversal

## What it is
Directory traversal (a.k.a. path traversal / LFI when it leads to file inclusion) is a class of web
vulnerability where user input is concatenated into a filesystem path without sufficient sanitization,
letting an attacker inject `../` sequences (or absolute paths, encoded variants, or unicode tricks)
to escape the intended base directory and read or include arbitrary files. In practice it is one of the
highest-value primitives on a box: it turns an unauthenticated request into arbitrary file read, which
exposes source code, configuration files holding secrets (`.env`, `wp-config.php`, `config.php`),
SSH keys, and `/etc/passwd` for user enumeration. Because filters are often applied naively, the
technique comes in many flavors — single-pass `..%2f` stripping that can be double-encoded, regex that
only blocks relative `../` but accepts absolute `/etc/passwd`, language quirks like Python's
`os.path.join` discarding earlier arguments when a later one is absolute, and null-byte injection
(`%00`) that truncates appended extensions on older stacks.

## When it works
- A web endpoint takes a **filename or path parameter** and reads/returns a file from the server
  (`?file=`, `?book=`, `download.php?id=`, `/static/...`, image/log viewers, export/ZIP generators).
- The application does **not** fully canonicalize or confine the resolved path to the intended base
  directory — the filter is missing, single-pass, regex-based, or bypassed by encoding/absolute paths.
- The attacker can **read files of value**: source code, `.env` / config, application secrets, SSH
  keys, or files that reveal other vulnerabilities and credentials.

## How it's done
Enumerate parameters that look like filenames, then probe the underlying behavior of the sanitizer.
Start with the obvious `../../../etc/passwd`; if blocked, work through the bypass ladder:
- **Encoding** — `..%2f`, `..%252f` (double URL-encode), `%2e%2e%2f`, or unicode/overlong forms to slip
  past naive `str_replace` and WAF filters.
- **Filter-strip inversion** — when the app strips a single `../`, feed it `....//` or `..././` so the
  strip pass collapses into a working `../`.
- **Absolute paths** — if the code does `base + user` or `os.path.join(base, user)`, supplying an
  absolute path (`/etc/passwd`, `C:\windows\win.ini`) makes the runtime discard `base` entirely,
  bypassing any `../` regex.
- **Null bytes** — on legacy stacks, `password.properties%00` truncates a forced `.ext` suffix.
- **Symlinks / static asset misconfig** — frameworks with `follow_symlinks=True` (e.g. AIOHTTP
  CVE-2024-23334) traverse via `/static/../../../`.
Confirm by reading `/etc/passwd` or `C:\windows\win.ini`, then pivot to source and config files
(`.env`, `wp-config.php`, `config_prod.json`, the app's own `.jar`/`.php`) to recover credentials
and next steps. Automated fuzzing with [[feroxbuster]] (directory/parameter discovery) and wordlist
traversal payloads speeds enumeration; file reads often feed directly into
[[database-credential-exposure]].

## Observed on
- [[agile]] — File read vulnerability in /vault/export endpoint
- [[arctic]] — Null byte injection to read password.properties file
- [[backdoor]] — Ebook Download plugin allows reading arbitrary files via path traversal
- [[bookworm]] — Traverse via bookIds parameter in multi-file ZIP download
- [[breadcrumbs]] — File read vulnerability in bookController.php with path traversal (book=..\..\path)
- [[broscience]] — Double URL-encoded path traversal (..%252f) in img.php to bypass filters and read PHP source
- [[chemistry]] — AIOHTTP CVE-2024-23334 via static assets with follow_symlinks=True
- [[fatty]] — Path traversal in file operations to download fatty-server.jar
- [[imagery]] — Admin path traversal via log_identifier parameter to read source code
- [[inject]] — Path traversal in image view parameter to read file system
- [[instant]] — Path traversal in admin log read endpoint
- [[intense]] — Path traversal in admin log viewing
- [[pov]] — Bypass ../ regex with absolute paths to read arbitrary files via download feature
- [[previous]] — Read arbitrary files including .env and NextAuth config
- [[store]] — URL-encoded path traversal in /file endpoint to read arbitrary files as encrypted output
- [[titanic]] — os.path.join behavior with absolute paths to bypass base directory
- [[undetected]] — Feroxbuster discovers /vendor directory with composer packages including PHPUnit
- [[unicode]] — Read arbitrary files via display endpoint using unicode bypass
- [[variatype]] — Single-pass filter bypass in download.php using ....// pattern
- [[yummy]] — Path traversal in export file creation allows reading arbitrary files from the host

## See also
[[database-credential-exposure]]
