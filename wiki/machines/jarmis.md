---
type: machine
title: Jarmis
platform: htb
os: linux
difficulty: medium
tags: [linux, web, ssrf, omi, python, privesc]
solved: 2026-07-09
sources: [[htb-jarmis]]
related: []
---
# Jarmis
> Medium Linux machine featuring a JARM fingerprinting API vulnerable to SSRF. The service makes an 11th request to "malicious" signatures, which can be redirected via Gopher to exploit the OMI service (OMIGod, CVE-2021-38647) for root access.

## Attack path
1. [[ssrf]] via JARM API fetch endpoint on localhost port scan
2. Discover OMI service on ports 5985/5986
3. Gopher protocol redirect from malicious JARM signature
4. Exploit [[omigod]] (CVE-2021-38647) for root command execution

## Techniques used
- [[ssrf]] — JARM API's `fetch` endpoint scans localhost and makes 11th request to malicious signatures
- [[gopher-redirect]] — Redirect curl User-Agent via Gopher protocol to send SOAP POST to OMI
- [[omigod]] — CVE-2021-38647: OMI service missing authentication headers allows arbitrary command execution
- port-scanning-via-api — Using JARM fetch endpoint to scan localhost by checking endpoint field in response

## Tools used
[[nmap]], curl, wfuzz, Python Flask, Metasploit, iptables, [[ncat]]

## Services / ports
[[ssh]] (22), [[http]] (80), omi (5985/5986)

## Lessons / notes
- JARM fingerprinting makes 10 TLS connections, then 11th HTTP request for metadata if signature is "malicious"
- localhost scans via JARM differ from 127.0.0.1 - code bug in get_jarm returns endpoint only for successful connections
- Gopher protocol useful for SSRF → POST conversion when target uses curl
- OMI (Open Management Infrastructure) ports 5985/5986 typically WinRM on Windows but different on Linux
- OMIGod vulnerability: missing Authorization header allows unauthenticated command execution
- Metasploit auxiliary/server/capture/http can be used for SSL redirect testing
