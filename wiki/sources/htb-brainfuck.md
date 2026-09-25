---
type: source
title: "HTB Brainfuck writeup"
raw: raw/htb-brainfuck.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[brainfuck]]
---
# Source: HTB Brainfuck writeup
> Legacy CTF-style Linux box featuring WordPress exploitation, Vigenère cipher decryption, RSA cryptographic weaknesses, and LXD container privilege escalation.
## Key facts extracted
- WordPress plugin privilege escalation vulnerability (WP Support Plus Responsive Ticket System < 8.0.0)
- SMTP credentials exposed in WordPress settings (orestis@brainfuck.htb / kHGuERB29DNiNE)
- Vigenère cipher encryption key "brainfuck" derived from forum signatures
- SSH key URL: https://10.10.10.17/8ba5aa10e915218697d1c658cdee0bb8/orestis/id_rsa
- SSH key passphrase: 3poulakia! 
- RSA parameters p, q, e leaked in debug.txt allowing calculation of private key d
- Alternative root path via LXD container exploitation
## Filed into
[[brainfuck]], [[wordpress-plugin-exploit]], [[vigenere-cipher]], [[rsa-cryptography-weakness]], [[lxd-container-privilege-escalation]]