---
type: source
title: "HTB Vault writeup"
raw: raw/htb-vault.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[vault]]
---
# Source: HTB Vault writeup
> Multi-VM environment with nested network requiring pivot through DNS and firewall to reach vault VM containing GPG-encrypted flag.

## Key facts extracted
- Network layout: ubuntu (192.168.122.1), DNS (192.168.122.4), firewall (192.168.122.5), vault (192.168.5.2)
- Credentials: dave:Dav3therav3123 (ubuntu), dave:dav3gerous567 (DNS)
- Firewall allows source ports 53 and 4444
- GPG encryption key: `itscominghome`
- SPICE ports: 5900-5902 (for console access)
- PHP5 extension bypasses upload filter

## Filed into
[[vault]], [[php-extension-bypass]], [[openvpn-rce]], [[firewall-bypass]], [[gpg-decrypt]], [[vm-escape]]
