---
type: source
title: "HTB Expressway writeup"
raw: raw/htb-expressway.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[expressway]]
---
# Source: HTB Expressway writeup
> IKE VPN server with aggressive mode PSK leak and dual sudo CVE exploitation paths.

## Key facts extracted
- IKE aggressive mode on UDP 500 leaks identity ike@expressway.htb
- PSK cracked with hashcat: freakingrockstarontheroad
- Two sudo CVEs: CVE-2025-32462 (hostname spoof) and CVE-2025-32463 (chroot nsswitch)
- TFTP hosts Cisco config file with VPN credentials

## Filed into
[[expressway]], [[ike-psk-crack]], [[cve-2025-32462]], [[cve-2025-32463]]