---
type: tool
title: Impacket
category: exploitation
tags: [ad, windows, network-protocols]
updated: 2026-07-09
---

# Impacket

## What it does
Python library + a large set of AD/Windows-protocol scripts (SMB, MSRPC, Kerberos, LDAP, WMI). The workhorse of offensive AD from Linux. Many scripts have Kerberos (`-k`/`-no-pass` + `KRB5CCNAME`) and pass-the-hash (`-hashes`) support.

## Key scripts
- `GetNPUsers.py` — [[as-rep-roasting]]
- `GetUserSPNs.py` — kerberoasting
- `secretsdump.py` — [[dcsync]] / local hash dump
- `smbclient.py` / `psexec.py` / `wmiexec.py` — SMB access & shells
- `dacledit.py` — DACL editing (see [[dacl-write-members]]; ShutdownRepo branch)
- `getTGT.py` — request a TGT

## Used on
- [[absolute]] — GetNPUsers (AS-REP), smbclient (SMB shares), dacledit (WriteMembers), and `secretsdump`/cme for DCSync.
- [[active]] — `GetUserSPNs.py` (kerberoasting), `psexec.py` (shell).
- [[forest]] — `GetNPUsers.py` (AS-REP), `secretsdump.py` (DCSync), `wmiexec.py`, `smbserver.py`.
