---
type: source
title: "HTB Carrier writeup"
raw: raw/htb-carrier.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[carrier]]
---
# Source: HTB Carrier writeup
> 0xdf's writeup for HTB Carrier covering SNMP enumeration, router exploitation, BGP hijacking, and network traffic interception in an ISP infrastructure simulation.

## Key facts extracted
- SNMP serial number: NET_45JDX23 provides admin web login
- Command injection in diag.php via base64-encoded check parameter
- Quagga BGP configuration allows route manipulation
- FTP traffic between AS200 and AS300 contains root credentials
- BGPtelc0rout1ng password works for FTP and root SSH
- Unintended solution: Add secondary IP to interface for direct FTP access

## Filed into
[[carrier]], [[snmp-enumeration]], [[command-injection]], [[bgp-hijacking]], [[network-enumeration]], [[credential-interception]], [[web]], [[ssh]], [[ftp]], [[bgp]], [[rce]], [[privesc]]
