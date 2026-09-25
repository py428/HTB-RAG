---
type: source
title: "HTB Sauna writeup"
raw: raw/htb-sau.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[sauna]]
---
# Source: HTB Sauna writeup

> Classic Active Directory penetration testing guide covering Kerberos attacks, registry credential extraction, BloodHound analysis, and DCSync domain compromise.

## Key facts extracted

- Domain: EGOTISTICAL-BANK.LOCAL, DC: SAUNA
- AS-REP roasting on fsmith with password `Thestrokes23`
- AutoLogon credentials: svc_loanmgr / `Moneymakestheworldgoround!`
- svc_loanmgr has DCSync privileges via GetChanges/GetChangesAll
- Administrator hash: `d9485863c1e9e05851aa40cbb4ab9dff`
- Multiple authentication methods: password, NTLM hash, Kerberos ticket

## Filed into

[[sauna]], [[kerberos-username-enumeration]], [[as-rep-roasting]], [[ldap-description-credential]], [[bloodhound]], [[dcsync]]
