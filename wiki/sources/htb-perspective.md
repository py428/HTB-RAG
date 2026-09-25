---
type: source
title: "HTB Perspective writeup"
raw: raw/htb-perspective.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[perspective]]
---
# Source: HTB Perspective writeup
> Complex ASP.NET exploitation chain featuring SHTML file upload for config leaks, cookie forgery with machineKey, SSRF to internal crypto service, ViewState deserialization, and padding oracle attacks on staging environment for command injection and root access.

## Key facts extracted
- Target: IIS 10.0 with ASP.NET 4.6.1 application (Production + Staging)
- Production keys: validationKey="99F1108B685094A8A31CDAA9CBA402028D80C08B40EBBC2C8E4BD4B0D31A347B0D650984650B24828DD120E236B099BFDD491910BF11F6FA915BF94AD93B52BF"
- Staging: AutoGenerate keys with different error verbosity
- Internal service: SecurePasswordService on localhost:8000 with XOR stream cipher
- ViewState: Requires generator, keys, and ViewStateUserKey for exploitation
- Password reset: Encrypted tokens vulnerable to padding oracle attack

## Filed into
[[perspective]], [[shtml-file-upload]], [[cookie-forgery]], [[ssrf]], [[deserialization]], [[padding-oracle]], [[command-injection]]
