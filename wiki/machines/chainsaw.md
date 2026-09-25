---
type: machine
title: Chainsaw
platform: htb
os: linux
difficulty: hard
tags: [linux, blockchain, web3, crypto, privesc]
solved: 2026-07-09
sources: [[htb-chainsaw]]
related: []
---
# Chainsaw

> Hard Linux box focused on blockchain/smart contract exploitation with Web3 interaction, IPFS file retrieval, and SUID binary exploitation for privilege escalation.

## Attack path
1. FTP smart contract files → [[smart-contract-exploitation]] → command injection → administrator shell
2. IPFS enumeration → encrypted SSH key → [[ssh-key-cracking]] → bobby user  
3. SUID [[path-hijacking]] OR smart contract manipulation → root shell
4. Slack space file recovery → actual root flag

## Techniques used
- [[smart-contract-exploitation]] — Ethereum smart contract command injection via setDomain function
- [[ipfs-enumeration]] — Found encrypted SSH key in IPFS blocks directory
- [[ssh-key-cracking]] — RSA private key crack using john and factordb
- [[path-hijacking]] — SUID binary calls sudo without absolute path, hijacked via PATH manipulation
- [[slack-space-recovery]] — Root flag hidden in file slack space using bmap tool

## Tools used
- [[nmap]] — Port scanning identifying FTP, SSH, and unknown Web3 port
- [[ftp]] — Anonymous FTP access to smart contract files
- web3 python — Ethereum blockchain interaction library
- [[john]] — SSH private key password cracking
- [[ssh]] — Remote access with cracked private key
- bmap — Slack space file recovery tool
- debugfs — File system block enumeration
- [[netcat]] — Reverse shell connections

## Services / ports
- [[ftp]] (21) — Anonymous access to smart contract files
- [[ssh]] (22) — Remote shell access
- http (9810) — Web3/Ethereum provider endpoint
- http (63991) — Local Web3 provider for ChainsawClub contract

## Lessons / notes
- Smart contract functions can be exploited for command injection if unsanitized input is executed
- IPFS stores files in blocks directory that can be enumerated for sensitive data
- Small RSA keys (256-bit) can be factored online using factordb.com
- SUID binaries calling system commands without absolute paths are vulnerable to PATH hijacking
- Slack space (file system space between file end and block end) can hide data not visible via normal file operations
- Web3 requires setting default account for transactions vs read calls
