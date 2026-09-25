---
type: source
title: "HTB Caption writeup"
raw: raw/htb-caption.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[caption]]
---
# Source: HTB Caption writeup
> 0xdf's comprehensive writeup for HTB Caption covering HTTP/2 smuggling, cache poisoning, CVE-2023-37474 exploitation, and command injection in a complex multi-stage attack.

## Key facts extracted
- Architecture: HAProxy → Varnish cache → Flask application
- GitBucket default credentials: root / root
- Margo user SSH key accessible via CVE-2023-37474 directory traversal
- Log service vulnerable to command injection via user-agent parsing
- Box patched one week after release to fix unintended paths

## Filed into
[[caption]], [[http-request-smuggling]], [[cache-poisoning]], [[xss]], [[parameter-tampering]], [[cve-2023-37474]], [[command-injection]], [[gitbucket]], [[ssh]], [[ad]], [[web]], [[rce]], [[privesc]]
