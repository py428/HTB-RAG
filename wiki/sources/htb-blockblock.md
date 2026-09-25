---
type: source
title: "HTB BlockBlock writeup"
raw: raw/htb-blockblock.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[blockblock]]
---
# Source: HTB BlockBlock writeup
> Complete exploitation of blockchain-based chat application covering XSS for JWT theft, Ethereum JSON-RPC interaction, blockchain data extraction, Foundry forge command abuse, and multiple Arch Linux pacman privilege escalation techniques.

## Key facts extracted
- Chat application vulnerable to stored XSS in message content
- Admin JWT token accessible via /api/info endpoint
- Ethereum JSON-RPC endpoint accessible on port 8545 with token authentication
- Blockchain contains embedded SSH credentials in transaction input data
- Forge build command accepts --use parameter for arbitrary binary execution
- Multiple pacman exploitation paths: package() file writes, install scripts, and --hookdir abuse
- Arch Linux requires different privilege escalation techniques than Debian-based systems

## Filed into
[[blockblock]], [[xss]], [[jwt-theft]], [[ethereum-json-rpc]], [[blockchain-data-extraction]], [[forge-command-abuse]], [[pacman-package-abuse]], [[pacman-hook-abuse]]
