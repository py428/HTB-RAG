---
type: technique
title: Kerberos Username Enumeration
tags: [ad, windows, kerberos, reconnaissance]
platforms: [windows]
mitre: [T1087.002]
updated: 2026-07-09
---

# Kerberos Username Enumeration

## What it is
Determine which usernames are **valid** in a domain by sending AS-REQ preauth attempts and reading the Kerberos error code. The KDC replies differently for a valid user (needs preauth / proceeds) vs. an unknown one (`KDC_ERR_C_PRINCIPAL_UNKNOWN`). No valid credentials required, and the account lockout risk is essentially nil.

## When it works
- You have a candidate list of usernames (often harvested from metadata, OSINT, a naming convention guess, or a breach).
- Port 88 (Kerberos) is reachable on the DC.

## How it's done
```
# Generate username permutations from "First Last" names
/opt/username-anarchy/username-anarchy -i users

# Enumerate valid ones against the DC
kerbrute userenum --dc dc.absolute.htb -d absolute.htb usernames
```
The source of the names here was **image metadata**: `exiftool` on downloaded website images exposed `Author`/`Artist` fields with employees' full names.

Tools: [[kerbrute]], [[exiftool]], `username-anarchy`. [[crackmapexec]] can do a coarser check (different error codes per status).

## Observed on
- [[absolute]] — full names lifted from hero-image EXIF `Author` tags → `username-anarchy` permutations → `kerbrute` confirmed the `[first-initial].[lastname]` format and six valid accounts.

## Variants & pitfalls
- Watch the response codes: `STATUS_ACCOUNT_RESTRICTION` vs `STATUS_LOGON_FAILURE` in SMB also leaks account existence even before Kerberos.
- Once you have valid users, immediately try [[as-rep-roasting]] — preauth-disabled accounts are the cheap next win.

## See also
[[as-rep-roasting]], [[kerbrute]], [[exiftool]]
