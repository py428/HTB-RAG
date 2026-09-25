---
type: source
title: "HTB Store writeup"
raw: raw/htb-store.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[store]]
---
# Source: HTB Store writeup
> Hard Linux box featuring ExpressJS file storage with XOR encryption, exploited via directory traversal to leak encrypted files and credentials, then SFTP tunneling to Node.js inspector, and finally Chrome debug port abuse for root access.
## Key facts extracted
- ExpressJS application on ports 5000-5002 with file upload/download functionality
- Static XOR encryption key "Hm9zeWC38" used across all files
- Directory traversal via URL encoding (%2f) in /file endpoint
- SFTP user (sftpuser) with tcp forwarding allowed for tunneling
- Node.js --inspect on localhost:9229 allows code execution
- ChromeWebDriver on port 9515 running as root
## Filed into
[[store]], [[directory-traversal]], [[xor-encryption]], [[ssh-tunneling]], [[nodejs-inspect]], [[chrome-debug]]
