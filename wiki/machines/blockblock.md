---
type: machine
title: BlockBlock
platform: htb
os: linux
difficulty: hard
tags: [linux, web, privesc, blockchain, smart-contracts, pacman, arch-linux]
solved: 2026-07-09
sources: [[htb-blockblock]]
related: []
---
# BlockBlock
> Blockchain chat application exploitation box featuring XSS, Ethereum JSON-RPC abuse, Foundry forge command exploitation, and Arch Linux pacman privilege escalation. Attack path: XSS to steal admin JWT, read blockchain for SSH credentials, abuse forge build command for user pivot, exploit pacman package installation for root.

## Attack path
1. [[xss]] — Stored XSS in chat application to steal admin JWT token
2. [[ethereum-json-rpc]] — Access Ethereum JSON-RPC to read blockchain data  
3. [[blockchain-data-extraction]] — Extract keira SSH credentials from raw blockchain blocks
4. [[forge-command-abuse]] — Abuse forge build --use for command execution as paul
5. [[pacman-privilege-escalation]] — Exploit pacman package installation for root shell

## Techniques used
- [[xss]] — Stored XSS in chat messages to execute JavaScript as admin user
- [[jwt-theft]] — Exfiltrate admin JWT via /api/info endpoint using XSS
- [[ethereum-json-rpc]] — Interact with Ethereum blockchain JSON-RPC API
- [[blockchain-data-extraction]] — Read raw blockchain blocks to extract embedded credentials
- [[forge-command-abuse]] — Abuse forge build --use to execute arbitrary binaries as paul
- [[pacman-package-abuse]] — Create malicious Arch Linux packages for privilege escalation
- [[pacman-hook-abuse]] — Use pacman --hookdir to execute scripts as root

## Tools used
[[nmap]], ffuf, netexec, curl, Python jwt library, forge, pacman, makepkg

## Services / ports
[[ssh]] (22), [[http]] (80), Ethereum JSON-RPC (8545)

## Lessons / notes
- Ethereum blockchains can store arbitrary data including credentials in transaction input
- JSON-RPC endpoints may require authentication tokens but expose sensitive blockchain data
- Foundry forge tool has multiple abuse vectors including --use and git command execution
- Arch Linux pacman can be abused for privilege escalation via malicious packages or hooks
- Blockchain applications may store sensitive data in smart contract storage or transaction input
- Package managers like pacman offer multiple exploitation paths for privilege escalation
- Arch Linux rolling release model requires different privilege escalation techniques than Debian-based systems
