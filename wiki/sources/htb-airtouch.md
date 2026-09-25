---
type: source
title: "HTB AirTouch writeup"
raw: raw/htb-airtouch.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[airtouch]]
---
# Source: HTB AirTouch writeup
> Comprehensive walkthrough of wireless penetration testing including SNMP reconnaissance, WPA2 cracking, traffic decryption, and evil twin attacks against enterprise wireless networks.

## Key facts extracted
- Exposes SNMP default password leak in sysDescr field
- Demonstrates complete WPA2-PSK attack chain from handshake capture to cracking
- Shows wireless traffic decryption using cracked PSK in Wireshark
- Details evil twin setup with eaphammer using recovered CA certificates
- Covers PEAP-MSCHAPv2 capture and cracking as NetNTLMv1

## Filed into
[[airtouch]], [[snmp-default-credentials]], [[wpa2-handshake-crack]], [[wireshark-decrypt]], [[evil-twin]], [[peap-mschapv2-crack]]
