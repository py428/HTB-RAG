---
type: technique
title: DCSync
tags: [ad, windows, credential-access, replication]
platforms: [windows]
mitre: [T1003.006]
updated: 2026-07-09
---

# DCSync

## What it is
Impersonate a Domain Controller by invoking the AD replication (`DRSUAPI`) protocol to **request password hashes** for any account straight from the DC — including `krbtgt` and `Administrator`. No code execution on the DC needed; it's a network call the DC services like any peer.

## When it works
You hold credentials (password or NT hash) for a principal with **replication rights**:
- Members of **Domain Admins / Enterprise Admins / Administrators**, **or**
- The **`DC$` machine account** itself (a DC can replicate from itself), **or**
- An account explicitly granted `DS-Replication-Get-Changes` / `…-All`.

## How it's done
```
# Impacket
secretsdump.py absolute.htb/DC\$@dc.absolute.htb -just-dc-ntds -hashes :<dc_hash>

# or crackmapexec (netexec), using the DC$ machine-account hash
crackmapexec smb -dc-ip dc.absolute.htb -u 'DC$' -H <dc_nt_hash> --ntds
```
Tools: [[impacket]] `secretsdump.py`, [[crackmapexec]].

## Observed on
- [[absolute]] — the `DC$` machine-account NT hash (recovered via [[kerberos-relay]]/[[shadow-credentials]]) dumped all NTDS hashes, yielding the `Administrator` hash → final `evil-winrm` shell.
- [[forest]] — `svc-alfresco` granted itself DCSync rights via Exchange WriteDacl, then `secretsdump`'d the Administrator hash.

## Variants & pitfalls
- The classic blocker on this box: every **user** was in Protected Users (NTLM off), but **`DC$` is not** — so once you have the machine-account hash, pass-the-hash DCSync works fine.
- `-just-dc-ntds` grabs only NTDS hashes (fast); drop it if you also want Kerberos keys / password history.

## See also
[[kerberos-relay]], [[shadow-credentials]], [[ntlm-disabled-protected-users]], [[impacket]], [[crackmapexec]]
