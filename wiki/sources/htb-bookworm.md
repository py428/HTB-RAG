---
type: source
title: "HTB Bookworm writeup"
raw: raw/htb-bookworm.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bookworm]]
---
# Source: HTB Bookworm writeup
> In-depth exploitation of Express.js bookstore with multiple vulnerability chaining.

## Key facts extracted
- Database credentials: bookworm / FrankTh3JobGiver
- Admin basket IDs exposed in HTML comments on /shop page
- Download endpoint: /download/:orderId?bookIds=X&bookIds=Y for ZIP files
- ebook-convert runs as neil on 127.0.0.1:3001
- sudo genlabel vulnerable to SQLi: UNION SELECT to inject PostScript
- PostScript template at /usr/local/labelgeneration/template.ps

## Filed into
[[bookworm]], [[xss-csp-bypass]], [[idor]], [[directory-traversal]], [[symlink-abuse]], [[postscript-injection]]
