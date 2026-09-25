---
type: source
title: "HTB Jarmis writeup"
raw: raw/htb-jarmis.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[jarmis]]
---
# Source: HTB Jarmis writeup
> Medium Linux machine centered around JARM fingerprinting technology. The API makes an 11th request to "malicious" signatures for metadata collection, which can be SSRF'd via Gopher redirect to exploit the OMI service (OMIGod CVE-2021-38647).

## Key facts extracted
- JARM API on /api/v1/fetch takes endpoint parameter and makes 10 TLS connections plus 11th HTTP request
- 222 signatures in database, 10 marked as malicious (Sliver, SilentTrinity, Ncat, Metasploit, Trickbot, AsyncRAT, Gophish, CobaltStrike)
- Malicious signatures trigger additional GET request with curl User-Agent
- localhost:5985/5986 discovered via API-based port scanning (endpoint field non-null for open ports)
- OMI (Open Management Infrastructure) service vulnerable to OMIGod (CVE-2021-38647)
- Gopher protocol redirect converts GET to POST for OMI SOAP request
- Flask server with SSL context on 8443 redirects to gopher://127.0.0.1:5985
- SOAP XML body executes commands via SCX_OperatingSystem::ExecuteShellCommand

## Filed into
[[jarmis]], [[ssrf]], [[omigod]], [[gopher-redirect]], [[port-scanning-via-api]]
