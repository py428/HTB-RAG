---
type: methodology
title: Active Directory Privilege Escalation
tags: [ad, active-directory, windows, privilege-escalation, methodology]
updated: 2026-07-09
---

# Active Directory Privilege Escalation

> Escalating from a foothold — anonymous, or any domain user — to **Domain Admin / DCSync**. This is the wiki's richest area: all three ingested boxes ([[absolute]], [[active]], [[forest]]) are AD chains, so the hubs below are battle-tested. Get local SYSTEM first via [[windows-local-privesc]] when the box is in the way.

## 1. Domain recon

```powershell
# BloodHound + SharpHound collector → visualize attack paths (the single best investment)
bloodhound-python -u <user> -p <pass> -d <dom> -ns <dc> -c All

# PowerView quick checks
Get-NetDomain
Get-NetUser | select samaccountname, description
Get-DomainGroupMember "Domain Admins"
```
Tools: [[bloodhound]], [[powerview]].

## 2. Credential harvesting (no privileges needed)

The fastest wins before touching ACLs — collect crackable hashes / plaintext creds:

| Step | Technique | Tool | Wiki |
|---|---|---|---|
| Find valid users | Kerberos username enumeration | [[kerbrute]] | [[kerberos-username-enumeration]] |
| Preauth-disabled accounts | AS-REP Roasting | [[impacket]] `GetNPUsers` / [[rubeus]] | [[as-rep-roasting]] |
| SPN accounts (often svc/admin) | Kerberoasting | [[rubeus]] / [[impacket]] `GetUserSPNs` | [[kerberoasting]] |
| Decrypted local-admin pwd from SYSVOL | GPP cpassword | [[crackmapexec]] / `gpp-decrypt` | [[gpp-cpassword]] |
| Passwords stashed in attributes | LDAP `description` creds | [[ldap]] queries | [[ldap-description-credential]] |
| Anonymous user/group recon | RPC null session | [[crackmapexec]] | [[rpc-null-session]] |

Crack harvested hashes with [[hashcat]] — mode **13100** (Kerberoast TGS) / **18200** (AS-REP).

## 3. ACL abuse — follow the BloodHound edges

Once you hold an account, BloodHound shows the privilege-escalation path to Domain Admins:

| Edge you hold | Escalation | Wiki |
|---|---|---|
| `WriteMembers` (or self on a group) | add yourself to a privileged group | [[dacl-write-members]] |
| `GenericWrite` / `GenericAll` on a user | set `msDS-KeyCredentialLink` → PKINIT → TGT as victim | [[shadow-credentials]] (via [[certipy]]) |
| `WriteDacl` / `WriteAccountRestrictions` on the domain | grant yourself DCSync rights (**Exchange** pattern) | [[writedacl-grant-dcsync]] |
| ADCS misconfig (ESC1–ESC8) | cert → TGT as any user | [[certipy]] (`find` / `auth`) |

## 4. Relay & coercion

- **Kerberos relay** — when [[ntlm-disabled-protected-users]] blocks NTLM: `KrbRelay` / `KrbRelayUp` coerces SYSTEM auth and relays it to LDAP to grant self privileges. → [[kerberos-relay]]
- **NTLM relay** (when NTLM is allowed) — `ntlmrelayx.py` against SMB/LDAP.

## 5. Endgame — domain compromise

- **DCSync** — impersonate a DC to dump NTDS hashes from the domain (requires replication rights). → [[dcsync]] (`impacket-secretsdump`, [[rubeus]] `dump`)
- **Cred pivot into boxes** — [[runascs]] (local RunAs with held creds), [[evil-winrm]] (WinRM session), [[crackmapexec]] (mass exec / pass-the-hash).

## Canonical chains observed in this wiki

- [[forest]] — `RPC null session` → `AS-REP roasting` → Exchange `WriteDacl → DCSync` rights → `DCSync`. *(Easy; 2016 DC + Exchange.)*
- [[active]] — anonymous SMB → `GPP cpassword` (local admin) → `Kerberoasting` an admin SPN. *(Easy; 2008 R2 DC.)*
- [[absolute]] — username enum + metadata → Kerberos-only path through `WriteMembers`, `Shadow Credentials`, finally `Kerberos relay` → `DCSync`. *(Insane; NTLM disabled.)*

## See also
- [[windows-local-privesc]] — get SYSTEM on the box first.
- Service hubs: [[kerberos]], [[ldap]], [[smb]].
