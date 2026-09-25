---
type: technique
title: Shadow Credentials
tags: [ad, windows, kerberos, pkinit, credential-access]
platforms: [windows]
mitre: [T1556]
updated: 2026-07-09
---

# Shadow Credentials

## What it is
Abuse write privileges on a target object to inject a self-created certificate into the target's `msDS-KeyCredentialLink` attribute (Key Trust). You then authenticate **as that target** via PKINIT (certificate-based Kerberos preauth), obtaining a TGT — and, through User-to-User (U2U), the target's **NT hash**. Less disruptive than resetting the victim's password.

## When it works
You have **`GenericWrite`** (or equivalent write ACL) on the target user/computer — e.g. inherited through a group you control, a `WriteDacl`, or `GenericAll`. Common AD misconfiguration chain.

## How it's done
One-shot with [[certipy]] (Linux):
```
KRB5CCNAME=/tmp/krb5cc_1000 certipy shadow auto \
  -username m.lovegod@absolute.htb -account winrm_user -k -target dc.absolute.htb
# → adds key credential, authenticates as winrm_user, returns NT hash + .ccache
```
Windows equivalents: Whisker / `PyWhisker`. The TGT/hash is then used to get a shell (e.g. [[evil-winrm]]).

## Observed on
- [[absolute]] — `m.lovegod` (added to the "Network Audit" group, which held `GenericWrite` on `winrm_user`) forged a shadow credential on `winrm_user` → WinRM foothold. Also used by [[kerberos-relay]] to forge a credential on the `DC$` **machine** account.

## Variants & pitfalls
- The ticket used to perform the write **must be fresh** — re-`kinit` (or `getTGT.py`) *after* gaining the group membership that grants `GenericWrite`, or you get `INSUFF_ACCESS_RIGHTS`.
- Restoring the original `msDS-KeyCredentialLink` after use avoids leaving an obvious trail (`certipy shadow auto` does this automatically).
- Works on **computer accounts** too — forging a shadow cred on `DC$` yields a machine-account hash usable for [[dcsync]].

## See also
[[dacl-write-members]], [[kerberos-relay]], [[dcsync]], [[certipy]]
