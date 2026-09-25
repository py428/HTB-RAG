---
type: machine
title: Store
platform: htb
os: linux
difficulty: hard
tags: [linux, web, privesc, file-upload, directory-traversal, xor-encryption, ssh-tunneling, nodejs, chrome-debug]
solved: 2026-07-09
sources: [[htb-store]]
related: []
---
# Store
> ExpressJS file storage site with XOR encryption, vulnerable to directory traversal to leak encrypted files and credentials, then using SFTP tunneling to access Node.js inspector and finally abusing Chrome debug port for root.
## Attack path
1. [[directory-traversal]] to leak /etc/passwd and other files (encrypted)
2. [[xor-encryption]] analysis to recover static XOR key
3. Decrypt files to find SFTP credentials in .env file
4. [[ssh-tunneling]] through SFTP to localhost Node.js inspector on port 9229
5. [[nodejs-inspect]] RCE to get shell as dev user
6. [[chrome-debug]] abuse (ChromeWebDriver) to get root shell
## Techniques used
- [[directory-traversal]] — URL-encoded path traversal in /file endpoint to read arbitrary files as encrypted output
- [[xor-encryption]] — Static XOR key "Hm9zeWC38" used for all file encryption
- [[ssh-tunneling]] — SFTP user with tcp forwarding allowed to tunnel to localhost:9229
- [[nodejs-inspect]] — Node.js running with --inspect flag allows remote code execution via Chrome DevTools
- [[chrome-debug]] — ChromeWebDriver running as root on port 9515 allows binary execution via session creation
## Tools used
- [[nmap]] — port scanning and service detection
- [[feroxbuster]] — directory brute force
- [[curl]] — HTTP requests and testing
- [[sftpclient]] — SFTP access and file listing
- sshpass, ssh — SFTP tunneling
- Chromium browser — accessing node inspector and chrome debug
- [[netcat]] — reverse shell listener
## Services / ports
- [[ssh]] (22) — SFTP access with tcp forwarding allowed
- [[http]] (5000, 5001, 5002) — ExpressJS applications
- sftp — File storage with credentials leakage
## Lessons / notes
- XOR encryption with repeating key can be recovered by XORing known plaintext with ciphertext
- Node.js --inspect flag allows full remote debugging and code execution
- SFTP with tcp forwarding can be used to tunnel to localhost services
- Chrome WebDriver session creation can execute arbitrary binaries as the running user
- ExpressJS directory traversal via URL encoding (%2f) bypassing path.normalize checks
