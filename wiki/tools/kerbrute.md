---
type: tool
title: Kerbrute
category: enumeration
tags: [ad, kerberos, username-enumeration]
updated: 2026-07-09
---

# Kerbrute

## What it does
Brute-forces/enumerates Kerberos — validates usernames (`userenum`) and passwords (`passwordspray`) against a DC via AS-REQ without triggering normal lockouts.

## Common usage
```
kerbrute userenum --dc dc.absolute.htb -d absolute.htb usernames.txt
kerbrute passwordspray --dc dc.absolute.htb -d absolute.htb users.txt password
```

## Used on
- [[absolute]] — `userenum` confirmed valid usernames and the `[first-initial].[lastname]` format (see [[kerberos-username-enumeration]]).
