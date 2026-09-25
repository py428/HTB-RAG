---
type: source
title: "HTB Chainsaw writeup"
raw: raw/htb-chainsaw.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[chainsaw]]
---
# Source: HTB Chainsaw writeup

> Comprehensive guide for HTB Chainsaw blockchain exploitation box covering Web3 smart contracts, IPFS enumeration, and slack space recovery.

## Key facts extracted
- FTP server hosts smart contract files (WeaponizedPing.sol, .json, address.txt)
- Ethereum smart contract vulnerable to command injection via setDomain function
- IPFS used to distribute encrypted SSH keys via email attachments
- 256-bit RSA key small enough to factor with online databases
- SUID ChainsawClub binary has two privilege escalation paths
- Root flag hidden in slack space of root.txt file
- bmap tool identifies and extracts data from file slack space

## Filed into
[[chainsaw]], [[smart-contract-exploitation]], [[ipfs-enumeration]], [[ssh-key-cracking]], [[path-hijacking]], [[slack-space-recovery]]
