---
type: technique
title: Kerberoasting
tags: [ad, windows, kerberos, credential-access]
platforms: [windows]
mitre: [T1558.003]
updated: 2026-07-09
---

# Kerberoasting

## What it is
Request a TGS (service ticket) for any account that has an SPN; the ticket contains material
encrypted with that account's password hash, which you crack offline. Unlike [[as-rep-roasting]] it
needs a valid domain account (to request the TGS), but it reaches far more targets — every
SPN-enabled account — and service accounts often have weak passwords.

## When it works
- You have any valid domain credentials (even low-privilege), AND
- A user/computer with an SPN has a crackable (weak) password.

## How it's done
```
# Impacket — request TGS hashes for all SPN accounts
GetUserSPNs.py -request -dc-ip <dc> <domain>/<user> -outputfile hashes.txt

# crack (hashcat 13100 = Kerberos 5 TGS, etype 23 / RC4)
hashcat -m 13100 hashes.txt /usr/share/wordlists/rockyou.txt
```
Windows: Rubeus `kerberoast`, Mimikatz `kerberos::hash`.

## Observed on
- [[active]] — with `SVC_TGS` creds, roasted the Administrator SPN (`active/CIFS:445`) →
  `Ticketmaster1968` → admin.

## Variants & pitfalls
- Prefer **etype 23 (RC4)** hashes — AES-encrypted tickets (etype 17/18) resist cracking. Request
  RC4 where the target allows it.
- Roasted accounts with admin-level rights = direct domain compromise.
- *Targeted* kerberoasting: roast one specific high-value SPN rather than all, to stay quieter.

## See also
[[as-rep-roasting]], [[impacket]], [[hashcat]]
